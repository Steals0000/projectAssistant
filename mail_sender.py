from flask_mail import Mail, Message

from config import app

class MailSender:
    mail = Mail(app)
    def send_message(self ,name, email, text, message):
        msg = Message("Отзыв", recipients=[app.config['MAIL_USERNAME']])
        msg.body = "Вы получили отзыв от {}.\n\nИмя: {}\nПочта: {}\nТема: {}\nОтзыв: {}".format(name, name, email, text, message)
        self.mail.send(msg)