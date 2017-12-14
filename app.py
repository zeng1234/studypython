# use/bin/env python3
#-*-coding:utf-8-*-
import tornado.web
import os
from allsocrepydemo.url import url
settings=dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "statics"),
)

app=tornado.web.Application(handlers=url,**settings)