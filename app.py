from flask import render_template, redirect, url_for, Flask, request, json,flash
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
import requests


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'dlyaproekta.diplom@gmail.com'  # введите свой адрес электронной почты здесь
app.config['MAIL_DEFAULT_SENDER'] = 'dlyaproekta.diplom@gmail.com'  # и здесь
app.config['MAIL_PASSWORD'] = 'nynfdinwztnsnhuc'  # введите пароль

mail = Mail(app)

bootstrap = Bootstrap(app)



def send_message(name,email,text,message):
    msg = Message("Отзыв", recipients=[app.config['MAIL_USERNAME']])
    msg.body = "Вы получили отзыв от {}.\n\nИмя: {}\nПочта: {}\nТема: {}\nОтзыв: {}".format(name, name, email, text, message)
    mail.send(msg)

def is_human(captcha_response):
    secret = "6LcaNWgmAAAAADJ4pENFVvC8vmEMyewBbOaU6o66"
    payload = {'response':captcha_response, 'secret':secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']

@app.route('/', methods=['GET', 'POST'])
def load_main_page():
    print('started')
    sitekey = '6LcaNWgmAAAAALSefXhFyL1tGzPthk0bevcfTvl5'
    if request.method == 'POST':
        print('post')
        name = request.form.get('name')
        email = request.form.get('email')
        text = request.form.get('text')
        message = request.form.get('message')
        captcha = request.form.get('g-recaptcha-response')
        print(name)
        print(email)
        print(text)
        print(message)
        print(captcha)
        send_message(name,email,text,message)
        if is_human(captcha):
            k = 't'
            print(k)
        else:
            k = 'f'
            print(k)
        return redirect(url_for('load_main_page'))
    return render_template('Home.html', sitekey = sitekey)

@app.route('/StepOne')
def load_first_page():
    return render_template('StepOne.html')

@app.route('/StepTwo')
def load_second_page():
    return render_template('StepTwo.html')

@app.route('/StepThree')
def load_third_page():
    return render_template('StepThree.html')

@app.route('/StepFour')
def load_fourth_page():
    return render_template('StepFour.html')

@app.route('/StepFive')
def load_five_page():
    return render_template('StepFive.html')

@app.route('/StepSix')
def load_six_page():
    return render_template('StepSix.html')

@app.route('/StepSeven')
def load_seven_page():
    return render_template('StepSeven.html')

if __name__ == '__main__':
    app.secret_key = 'asrtarstaursdlarsn'
    app.run(debug=True)
