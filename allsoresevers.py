# use/bin/env python3
#-*-coding:utf-8-*-
import tornado.httpserver
import tornado.ioloop
from tornado.options import options,define
from allsocrepydemo.app import app
import logging
define("port" ,default=8092,type=int,help="severs run")
def main():
    options.parse_command_line()
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    logging.info("connet to")
    tornado.ioloop.IOLoop.instance().start()
if __name__=="__main__":
    main()