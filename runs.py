import tornado.ioloop
from application import application
port = 80
if __name__ == "__main__":
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()