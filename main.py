from database import get_connection


class RepositoryPostgresql:
    def __init__(self):
        self.__conn = get_connection()

    def get_all_data(self):
        pool = self.__conn.get_pool_conn()
        try:
            cur = pool.cursor()
            sql = """
                select * from tbl_job_desc limit 10
            """
            cur.execute(sql)
            return cur.fetchall()
        except Exception as error:
            raise error
        finally:
            self.__conn.put_pool_conn(pool)

    def get_one_data(self, id):
        pool = self.__conn.get_pool_conn()
        try:
            cur = pool.cursor()
            sql = """
                select * from tbl_job_desc where id = %s limit 1
            """%(id)
            cur.execute(sql)
            return cur.fetchone()
        except Exception as error:
            raise error
        finally:
            self.__conn.put_pool_conn(pool)


if __name__ == '__main__':
    databaseRepo = RepositoryPostgresql()

    data = databaseRepo.get_all_data()
    print(data)

    data = databaseRepo.get_one_data(1)
    print(data)
