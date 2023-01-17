import psycopg2 
from psycopg2.extras import RealDictCursor
import os

class DB:
    setting = {
        'dbname': os.environ['DB_NAME'],
        'username': os.environ['DB_USER'],
        'password': os.environ['DB_PASS'],
        'host': os.environ['DB_HOST'],
        'port': os.environ['DB_PORT']
    }
    def execute_query(self, query, args={}):
        db = psycopg2.connect(
            dbname=self.setting['dbname'], user=self.setting['username'], password=self.setting['password'], host=self.setting['host'], port=self.setting['port'])
        try:
            cursor = db.cursor(cursor_factory=RealDictCursor)
        except :
            raise Exception('error DB connection!')
        try:
            cursor.execute(query, args)
            try  :
                row = cursor.fetchall()
            except :
                row = 0 
            db.commit() 
        except Exception as e:
            db.rollback()  
            print(query)
            print(args)
            print(e) 
            raise Exception('error DB query! \n *query :' +query+'\n *arguments : '+str(args)+'\n *ERROR : ')
        finally: 
            cursor.close() 
            db.close()
        return row
    