# use/bin/env python3
#-*-coding:utf-8-*-
import tornado.web
import logging
import base64
import os
from allsocrepydemo.methods.ordersign import ordersign
class BankPay(tornado.web.RequestHandler):
    def get(self):
        self.render("bankpay.html")
    def post(self):
        orderdict={
            "merchantId": self.get_argument("merchantId"),
            "subject": self.get_argument("subject"),
            "transAmt": self.get_argument("transAmt"),
            "outOrderId": self.get_argument("outOrderId"),
            "body": self.get_argument("body"),
            "outAcctId": self.get_argument("outAcctId"),
            "payMethod": self.get_argument("payMethod"),
            "defaultBank": self.get_argument("defaultBank"),
            "channel": self.get_argument("channel"),
            "cardAttr": self.get_argument("cardAttr"),
            "signType": self.get_argument("signType"),
            "returnUrl": self.get_argument("returnUrl"),
            "notifyUrl": self.get_argument("notifyUrl"),
            "detailUrl": self.get_argument("detailUrl"),
            "version": self.get_argument("version"),
            "service" : "directPay",
            "inputCharset": "UTF-8"
        }
        logging.info(orderdict)

        path=os.path.abspath("rsa_private_key.pem")
        sign=ordersign(orderdict,path)
        sign=base64.b64encode(sign)
        logging.info(sign)
        self.render("topay.html",sign=sign,**orderdict,signType=self.get_argument("signType"))


