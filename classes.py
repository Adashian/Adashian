from random import randint
import requests
import json

from sign import generate_sign
from config import SHOP_ID, SECRET_KEY, PAYWAY


class Pay:

    def __init__(self, amount, currency, description=None):
        self.currency = currency
        self.amount = format(amount, '.2f')
        self.description = description
        self.shop_id = SHOP_ID
        self.secret_key = SECRET_KEY
        self.shop_order_id = randint(1, 9999)

    def ptx(self):
        self.request_dict = {
            'amount': self.amount,
            'currency': self.currency,
            'shop_id': self.shop_id,
            'shop_order_id': self.shop_order_id
        }
        self.data = generate_sign(self.request_dict)
        self.data['description'] = self.description
        self.data['url'] = 'https://pay.piastrix.com/ru/pay'
        with open('logs/logs.json', 'a+', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)
        return self.data

    def bill(self):
        self.request_dict = {
            'shop_amount': self.amount,
            'shop_currency': self.currency,
            'shop_id': self.shop_id,
            'shop_order_id': self.shop_order_id,
            'payer_currency': self.currency
        }
        self.data = generate_sign(self.request_dict)
        self.data['description'] = self.description
        response = requests.post('https://core.piastrix.com/bill/create', json=self.data)
        response = response.json()
        with open('logs/logs.json', 'a+', encoding='utf-8') as f:
            json.dump(response, f, ensure_ascii=False, indent=4)
        return response['data']['url']

    def invoice(self):
        self.request_dict = {
            'amount': self.amount,
            'currency': self.currency,
            'payway': PAYWAY,
            'shop_id': self.shop_id,
            'shop_order_id': self.shop_order_id
        }
        self.data = generate_sign(self.request_dict)
        self.data['description'] = self.description
        response = requests.post('https://core.piastrix.com/invoice/create',
                                 json=self.data, headers={'Content-Type': 'application/json'})
        response = response.json()
        with open('logs/logs.json', 'a+', encoding='utf-8') as f:
            json.dump(response, f, ensure_ascii=False, indent=4)
        return response['data']
