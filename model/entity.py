import torndb
class MysqlHander:
    def __init__(self):
        self.db = torndb.Connection("localhost","huahu","root","")

    def show(self):
        rows = self.db.query("select * from huahu",)
        return rows