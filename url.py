# use/bin/env python3
#-*-coding:utf-8-*-
from allsocrepydemo.handlers.bankpay import BankPay
from allsocrepydemo.handlers.returlrsa import ReturnUrl
from allsocrepydemo.handlers.orderquery import OrderQuery
from allsocrepydemo.handlers.fastpay import FastPay
from allsocrepydemo.handlers.fasttopay import FastToPay
url=[
    (r'/bankpay',BankPay),
    (r'/',BankPay),
    (r'/return',ReturnUrl),
    (r'/orderquery',OrderQuery),
    (r'/fastsms',FastPay),
    (r'/fastpay',FastToPay)
]