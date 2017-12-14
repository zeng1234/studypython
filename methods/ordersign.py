# use/bin/env python3
#-*-coding:utf-8-*-
import logging
from allsocrepydemo.methods.rsautill import dosign
def ordersort(orderdict):
    l=[]
    for k in orderdict:
        l.append(k+"="+orderdict[k])
    l.sort()
    orderstr="&".join(l)
    return orderstr
def ordersign(orderdict,privatekeypath):
    orderdict.pop("signType")
    str=ordersort(orderdict)

    sign=dosign(str,privatekeypath)
    logging.info(sign)
    return sign
'''
if __name__ == "__main__":
    a={"a":"a","signType":"signType","b":"b"}
    print(ordersign(a))
    '''




