# use/bin/env python3
#-*-coding:utf-8-*-
import os
import tornado.web
import base64
import logging
from allsocrepydemo.methods.rsautill  import encryptbypublic
from allsocrepydemo.methods.urltool import urlencoding
from allsocrepydemo.methods.ordersign import ordersort,ordersign
from allsocrepydemo.methods.httpposttool import dopost
from allsocrepydemo.handlers.urladr import fastpay
from allsocrepydemo.methods.parasexml import fastOrderxml
class FastToPay(tornado.web.RequestHandler):
    def post(self):
        pathpublic = os.path.abspath("allscore_public_key.pem")
        pathprivate = os.path.abspath("rsa_private_key.pem")
        fastpaydict = {
            "merchantId": self.get_argument("merchantId"),
            "transAmt": self.get_argument("transAmt"),
            "outOrderId": self.get_argument("outOrderId"),
            "outAcctId": self.get_argument("outAcctId"),
            "payMethod": self.get_argument("payMethod"),
            "inputCharset": self.get_argument("inputCharset"),
            "signType": self.get_argument("signType"),
            "service": self.get_argument("service"),
            "orderId": self.get_argument("orderId"),
            "verifyCode": encryptbypublic(self.get_argument("verifyCode"), pathpublic).decode("utf-8"),
        }
        fasttopaystr=ordersort(urlencoding(fastpaydict))
        sign=ordersign(fastpaydict,pathprivate)
        logging.info(sign)
        sign=base64.b64encode(sign).decode("utf-8")
        fasttopaystr=fasttopaystr+"&sign="+sign
        logging.info(fasttopaystr)
        data=dopost(fasttopaystr,fastpay)
        logging.info(data)
        repdict=fastOrderxml(data)
        logging.info(repdict)


