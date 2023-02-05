from django.test import TestCase

import requests

def upd():
    url = "http://127.0.0.1:8000/notifications/update_mailings/"
    data = {"id": "a83ad7ca-a575-4f2c-add6-e07cbbacff74"}
    a = requests.post(url, data=data)


    pass

upd()