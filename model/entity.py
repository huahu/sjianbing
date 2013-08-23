import torndb
class MysqlHander:
    def __init__(self):
        self.db = torndb.Connection("localhost","huahu","root","")

    def delete(self,table):
        self.db.execute("drop table %s" % table)

    def update(self, table, dict):
        for i in dict.keys():
            self.db.execute("UPDATE %s set Sended = %d where email = '%s'"%(table, dict[i],i))

    def show(self):
        rows = self.db.query("select * from huahu",)
        return rows