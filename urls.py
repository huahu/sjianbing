from handlers.index import MainHandler
from handlers.index import ShowData



urls = [
    (r'/index', MainHandler),
    (r'/data',ShowData),
]


