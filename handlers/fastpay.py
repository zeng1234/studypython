# use/bin/env python3
#-*-coding:utf-8-*-
import tornado.web
import os
import base64
import logging
from allsocrepydemo.methods.rsautill import encryptbypublic
from allsocrepydemo.methods.ordersign import ordersign,ordersort
from allsocrepydemo.methods.httpposttool import dopost
from allsocrepydemo.methods.urltool import urlencoding
from allsocrepydemo.handlers.urladr import fastsms
from allsocrepydemo.methods.parasexml import fastOrderxml
class FastPay(tornado.web.RequestHandler):
    def get(self):
        self.render("fastpay.html")
    def post(self):
        pathpublic=os.path.abspath("allscore_public_key.pem")
        pathprivate=os.path.abspath("rsa_private_key.pem")
        fastpaydict={
            "merchantId": self.get_argument("merchantId"),
            "subject": self.get_argument("subject"),
            "transAmt": self.get_argument("transAmt"),
            "outOrderId": self.get_argument("outOrderId"),
            "body": self.get_argument("body"),
            "outAcctId": self.get_argument("outAcctId"),
            "payMethod": self.get_argument("payMethod"),
            "bankId": self.get_argument("bankId"),
            "inputCharset": self.get_argument("inputCharset"),
            "cardType": self.get_argument("cardType"),
            "signType": self.get_argument("signType"),
            "service": self.get_argument("service"),
            "notifyUrl": self.get_argument("notifyUrl"),
            "bankCardNo": encryptbypublic(self.get_argument("bankCardNo"),pathpublic).decode("utf-8"),
            "realName": encryptbypublic(self.get_argument("realName"),pathpublic).decode("utf-8"),
            "cardId": encryptbypublic(self.get_argument("cardId"),pathpublic).decode("utf-8"),
            "phoneNo": encryptbypublic(self.get_argument("phoneNo"),pathpublic).decode("utf-8"),
            "version": self.get_argument("version")
        }
        #logging.info(encryptbypublic(self.get_argument("bankCardNo"),pathpublic).decode("utf-8"))

        fastpaystr=ordersort(urlencoding(fastpaydict))
        logging.info(fastpaystr)
        logging.info(fastpaydict)
        sign=ordersign(fastpaydict,pathprivate)
        sign=base64.b64encode(sign).decode("utf-8")
        logging.info(sign)
        fastpaystr=fastpaystr+"&sign="+sign
        logging.info(fastpaystr)
        data=dopost(fastpaystr,fastsms)
        repdict=fastOrderxml(data)
        logging.info(repdict)
        outAcctId=self.get_argument("outAcctId")
        self.render("fasttopay.html",outAcctId=outAcctId,**repdict)




