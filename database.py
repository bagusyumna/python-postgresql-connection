from psycopg2.pool import ThreadedConnectionPool


class Database:
    def __init__(self, database: str = 'postgres', host: str = 'localhost', password: str = 'secret', user: str = 'root', port: str = '5432'):
        self.__database = database
        self.__host = host
        self.__password = password
        self.__user = user
        self.__port = port
        self.__pool = self.__create_connection()

    def __create_connection(self):
        try:
            print("create con")
            pool_connection = ThreadedConnectionPool(
                minconn=1,
                maxconn=10,
                dsn=f'postgresql://{self.__user}:{self.__password}@{self.__host}:{self.__port}/{self.__database}?application_name=flasksimpleapi')
            return pool_connection
        except Exception as e:
            raise ValueError(e)

    def get_pool_conn(self):
        return self.__pool.getconn()

    def put_pool_conn(self, conn):
        return self.__pool.putconn(conn)

database_obj = Database()

def get_connection() -> Database:
    return database_obj
