from flask import Flask, render_template, request
from flask_mail import Mail, Message
from config import mail_password, mail_username
import os

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password
mail = Mail(app)


@app.route("/", methods=['GET', 'POST'])
@app.route('/home')
def home():
    displayMessage = ''
    msg2 = ''
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        msg2 = f' We will be in touch using this email {email}'
        msg = Message(
            subject=f'Mail from {name}',
            body=f'reply to {email}\n\n\n{message}',
            sender=mail_username,
            recipients=['gowardwebdesign@gmail.com'])
        displayMessage = f'Thank you for contacting, {name}! '
        mail.send(msg)
        return render_template('homepages/home.html',
                               success=True,
                               displayMessage=displayMessage, message2=msg2)

    return render_template('homepages/home.html')


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
