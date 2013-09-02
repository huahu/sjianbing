#coding:utf-8
from tornado.web import RequestHandler
import os.path
from wtforms import TextField
from hform import Form
from model import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class HuahuForm(Form):
    name = TextField('name')
    number = TextField('number')

class MainHandler(RequestHandler):
    def get(self):
        self.render("index.html")

class ReciveData(RequestHandler):
    def post(self):
        self.db=create_engine('mysql+mysqldb://root:@localhost/huahu',echo=True)
        self.Session = sessionmaker(bind=self.db)
        self.session = self.Session()
        form = HuahuForm(self.request.arguments, locale_code=self.locale.code)
        number = form.number.data
        name = form.name.data
        ed_user = User(number, name)
        self.session.add(ed_user)
        self.session.commit()

class NotFoundHandler(RequestHandler):
    def prepare(self):
        NOTFOUND_404 = "404.html" # 404文件地址
        if os.path.exists(NOTFOUND_404):
            self.set_status(404) # 设 404 状态,浏览器可能会跳转到自己定义的找不到页面,要想全部显示一样就不要
            self.render(NOTFOUND_404, url = self.request.full_url())
        else:
            self.send_error(404)

