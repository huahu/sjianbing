#coding:utf-8
from urls import urls
import tornado.web
import os

SETTING = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    xsrf_cookies=True,
)
application = tornado.web.Application(
    handlers=urls,
    **SETTING
)