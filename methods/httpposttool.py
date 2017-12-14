# use/bin/env python3
#-*-coding:utf-8-*-
from urllib import request
import logging

def dopost(str,urladr):
    logging.info("connect to %s"%urladr)
    rep=request.Request(urladr)
    #request.quote(str,encoding="utf-8")
    #logging.info(str)
    with request.urlopen(rep,data=str.encode("utf-8")) as f:
        data=f.read().decode("utf-8")
        data=request.unquote(data, encoding="utf-8")
        logging.info(data)#收到的返回信息
        '''
        拆分返回获取tn
        '''
    return data
