from DB import DB

class Lathion :
    def main(self) :
        pass
    def db_test(self) :
        #DB와 Server간 통신을 확인한다.
        db = DB()
        return db.execute_query('SELECT * FROM tb_users')