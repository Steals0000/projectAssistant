from flask import render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

from config import app
from mail_sender import MailSender
from captcha_validator import CaptchaValidator

bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def load_main_page():
    captcha_validator = CaptchaValidator()
    if request.method == 'POST':
        mail_send = MailSender()
        mail_send.send_message(request.form.get('name'), request.form.get('email'), request.form.get('text'), request.form.get('message'))
        captcha_validator.is_human(request.form.get('g-recaptcha-response'))
        return redirect(url_for('load_main_page'))
    return render_template('Home.html', sitekey = captcha_validator.sitekey)

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
    app.run(debug=True)
