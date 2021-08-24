
# TO SEND EMAIL FROM A GMAIL ACCOUNT
# fill in your username and password below, and
# enable "less secure apps" at https://myaccount.google.com/lesssecureapps

GMAIL_USERNAME = ""
GMAIL_PASSWORD = ""



from flask import Flask
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = GMAIL_USERNAME
app.config['MAIL_PASSWORD'] = GMAIL_PASSWORD
mail = Mail(app)


from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

class EmailForm(FlaskForm):
    address = StringField('To')
    body = TextAreaField('Message')
    submit = SubmitField('Send')


from flask import render_template, flash
from flask_mail import Message

@app.route('/', methods=['GET', 'POST'])
def home():
    sender = GMAIL_USERNAME+"@gmail.com"
    form = EmailForm()
    if form.validate_on_submit():
        msg = Message("sent from a flask app", sender=sender,
                      recipients=[form.address.data])
        msg.body = form.body.data
        mail.send(msg)
        flash('Message sent to ' + form.address.data)
    return render_template("email.html", form=form, sender=sender)


# set FLASK_APP=app_with_email
# flask run
