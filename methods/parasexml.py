# use/bin/env python3
#-*-coding:utf-8-*-
from xml.etree import ElementTree
def parsexml(data):
    responsedict={}
    root=ElementTree.fromstring(data)
    lst_note=root.getiterator("queryResult") #获得跟节点循环器
    for k in lst_note:
        for n in k.getchildren():#获得跟节点的只节点
            responsedict[n.tag]=n.text
    return responsedict

def fastOrderxml(data):
    responsedict={}
    root=ElementTree.fromstring(data)
    lst_note=root.getiterator("fastOrder") #获得跟节点循环器
    for k in lst_note:
        for n in k.getchildren():#获得跟节点的只节点
            responsedict[n.tag]=n.text
    return responsedict
xm=r'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <queryResult>
        <srcOutOrderId>4546848548747848548</srcOutOrderId>
        <errorInfo>INVALID_OUT_ORDER_ID</errorInfo>
    </queryResult>
'''
