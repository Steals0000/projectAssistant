from flask import json
import requests

class CaptchaValidator:
    secret = "6LcaNWgmAAAAADJ4pENFVvC8vmEMyewBbOaU6o66"
    sitekey = '6LcaNWgmAAAAALSefXhFyL1tGzPthk0bevcfTvl5'
    def is_human(self, captcha_response):
        payload = {'response': captcha_response, 'secret': self.secret}
        response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
        response_text = json.loads(response.text)
        return response_text['success']