import sqlalchemy as db


class Database():
    def __init__(self, id, passwd, host, db_name):
        self.engine = db.create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.format(id, passwd, host, db_name))
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()


    def get_table(self, table_name):
        table = db.Table(table_name, self.metadata, autoload=True, autoload_with=self.engine)
        return table