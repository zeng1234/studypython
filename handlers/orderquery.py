# use/bin/env python3
#-*-coding:utf-8-*-
import tornado.web
import os
import base64
import logging
from allsocrepydemo.handlers.urladr import *
from  allsocrepydemo.methods.ordersign import ordersign,ordersort
from  allsocrepydemo.methods.httpposttool import dopost
from allsocrepydemo.methods.parasexml import parsexml
class OrderQuery(tornado.web.RequestHandler):
    def get(self):
        self.render("orderquery.html")

    def post(self):
        orderquerydict={
            "merchantId": self.get_argument("merchantId"),
            "service": self.get_argument("service"),
            "inputCharset": self.get_argument("inputCharset"),
            "outOrderId": self.get_argument("outOrderId"),
            "signType": self.get_argument("signType"),
            "version" : self.get_argument("version")
        }
        path = os.path.abspath("rsa_private_key.pem")
        sign=ordersign(orderquerydict,path )
        sign = base64.b64encode(sign)
        sign=sign.decode("utf-8")
        orderquerystr = ordersort(orderquerydict)+"&sign="+sign+"&signType="+self.get_argument("signType")
        logging.info(orderquerystr)
        data=dopost(orderquerystr,orderqueryurl)
        logging.info(sign)
        logging.info(data)
        self.render("orderresponse.html",**parsexml(data))




