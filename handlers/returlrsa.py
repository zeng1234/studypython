# use/bin/env python3
#-*-coding:utf-8-*-
import tornado.web
class ReturnUrl(tornado.web.RequestHandler):
    def get(self):
        self.get_argument()
        self.write("good")