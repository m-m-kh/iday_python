#### https://idpay.ir/web-service/v1.1  حتما مطالعه شود ####

import requests


MAKE_TRANSACTION = 'https://api.idpay.ir/v1.1/payment'
VERIFY = 'https://api.idpay.ir/v1.1/payment/verify'
INQUIRY = "https://api.idpay.ir/v1.1/payment/inquiry"
TRANSACTIONS = 'https://api.idpay.ir/v1.1/payment/transactions'


class IdPay(requests.Session):
    def __init__(self, api_key):
        super().__init__()
        data = {
            'Content-Type': 'application/json',
            'X-API-KEY': api_key,
            'X-SANDBOX': '0',
        }
        self.headers.update(data)
    
    
    def make_transaction(self, order_id:str, amount:int, callback:str, name:str = None, phone:str = None, mail:str = None, desc:str = None):
        '''
order_id string ضروری شماره سفارش پذیرنده به طول حداکثر 50 کاراکتر\n
amount number ضروری مبلغ مورد نظر به ریال مبلغ باید بین 1,000 ریال تا 500,000,000 ریال باشد\n
name string غیر ضروری نام پرداخت کننده به طول حداکثر 255 کاراکتر\n
phone string غیر ضروری تلفن همراه پرداخت کننده به طول 11 کاراکتر\n
مثل 9382198592 یا 09382198592 یا 989382198592\n
mail string غیر ضروری پست الکترونیک پرداخت کننده به طول حداکثر 255 کاراکتر\n
desc string غیر ضروری توضیح تراکنش به طول حداکثر 255 کاراکتر\n
callback string ضروری آدرس بازگشت به سایت پذیرنده
'''
        data = {
            'order_id':order_id,
            'amount': amount,
            'callback': callback,
            'name' : name,
            'phone':phone,
            'mail':mail,
            'desc':desc
        }
        response = self.post(MAKE_TRANSACTION,json=data)
        return response.json()
    
    
    def inquiry(self, id:str, order_id:str):
        '''id string ضروری کلید منحصر بفرد تراکنش که در مرحله ایجاد تراکنش دریافت شده است\n
order_id string ضروری شماره سفارش پذیرنده که در مرحله ایجاد تراکنش ارسال شده است'''
        data = {
            'id':id,
            'order_id':order_id
        }
        response = self.post(INQUIRY, json=data)
        return response.json()
    
    
    def verification(self, id:str, order_id:str):
        '''id string ضروری کلید منحصر بفرد تراکنش که در مرحله ایجاد تراکنش دریافت شده است\n
order_id string ضروری شماره سفارش پذیرنده که در مرحله ایجاد تراکنش ارسال شده است'''
        data = {
            'id':id,
            'order_id':order_id
        }
        response = self.post(VERIFY, json=data)
        return response.json()
    
    def get_transactions(self):
        '''1	پرداخت انجام نشده است\n
2	پرداخت ناموفق بوده است\n
3	خطا رخ داده است\n
4	بلوکه شده\n
5	برگشت به پرداخت کننده\n
6	برگشت خورده سیستمی\n

7	انصراف از پرداخت\n
8	به درگاه پرداخت منتقل شد\n
10	در انتظار تایید پرداخت\n
100	پرداخت تایید شده است\n
101	پرداخت قبلا تایید شده است\n
200	به دریافت کننده واریز شد\n
'''
        response = self.post(TRANSACTIONS)
        return response.json()
        




