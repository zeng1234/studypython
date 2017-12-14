# use/bin/env python3
#-*-coding:utf-8-*-
from urllib import request
def urlencoding(urldict):
    orderdict={}
    for k in urldict:
        orderdict[k]=request.quote(urldict[k])
    return orderdict

if __name__=="__main__":
    order = {
        "merchantId": "sdiajdei+jijijdoi=",
        "subject": "subject",
        "transAmt": "transAmt",
        "outOrderId": "outOrderId",
        "body": "body",
        "outAcctId": "outAcctId"
    }


