import sqlalchemy as db


class Database():
    def __init__(self, id, passwd, host, db_name):
        self.engine = db.create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.format(id, passwd, host, db_name), pool_pre_ping=True)
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()


    def get_table(self, table_name):
        table = db.Table(table_name, self.metadata, autoload=True, autoload_with=self.engine)
        return table

    def insert(self, table, values):
        query = db.insert(table).values(values).prefix_with('IGNORE')
        result_proxy = self.connection.execute(query)
        return result_proxy.rowcount

    def update_since_id(self, table, value, condition=None):
        query = db.update(table).values(since_id=value).where(condition)
        result_proxy = self.connection.execute(query)
        return result_proxy.rowcount

    def select(self, table, condition=None):
        if condition is not None:
            query = db.select([table]).where(condition)
        else:
            query = db.select([table])

        result_proxy = self.connection.execute(query)
        result_set = result_proxy.fetchall()
        return [result[0] for result in result_set]


