from flask import Flask, render_template, request, flash
from flask_mysqldb import MySQL
from review_form import RegisterForm

app = Flask(__name__)

# Storing MySQL credentials in flask app config.
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'XXXXXXXXXXXXXXXXXXXX'
app.config['MYSQL_PASSWORD'] = 'XXXXXXXXXXXXXXXXXXXXX'
app.config['MYSQL_DB'] = 'review_collection'

# Storing recaptcha credentials
app.config['SECRET_KEY'] = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'
app.config['RECAPTCHA_PRIVATE_KEY'] = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'black'}

# Initialising the MySQL instance for the app.
mysql = MySQL(app)

# Funtion to insert review into the db.
def save_review(name, email, url, rating, review):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO user_reviews(name, email, website, rating, review) VALUES (%s, %s, %s, %s, %s)",
                (name, email, url, rating, review))
    mysql.connection.commit()
    cur.close()


# Routing and method for review_collection.
@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    try:
        form = RegisterForm()
        if request.method == "POST":
            if not request.form.get('g-recaptcha-response'):
                return render_template('message.html', message="Huh, got you son of a bot.")
            details=request.form
            name = details['name']
            email = details['email']
            url = details['website']
            rating = details['rating']
            review = details['review']
            save_review(name, email, url, rating, review)
            return render_template('message.html', message="Thank you for your feedback.")
    except Exception as ex:
        return render_template('message.html', message="Oops!  Something went wrong.  Try again..." + str(ex))
    return render_template('review_collection.html', form=form)


app.run(host='0.0.0.0', port=8080)



