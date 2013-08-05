import tornado.ioloop
from application import application
post = 8088
if __name__ == "__main__":
    application.listen(post)
    tornado.ioloop.IOLoop.instance().start()