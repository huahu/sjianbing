#coding:utf-8
import tornado
import tornado.web
import os.path
from model.entity import MysqlHander

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = MysqlHander().show()
        self.render("index.html",items=items)

class ShowData(tornado.web.RequestHandler):
    def get(self):
        db = MysqlHander().show()
        self.write(str(db))

# 找不到页面的处理
class NotFoundHandler(tornado.web.RequestHandler):
    def prepare(self):
        NOTFOUND_404 = "404.html" # 404文件地址
        if os.path.exists(NOTFOUND_404):
            #self.set_status(404) # 设 404 状态,浏览器可能会跳转到自己定义的找不到页面,要想全部显示一样就不要
            self.render(NOTFOUND_404, url = self.request.full_url())
        else:
            self.send_error(404)