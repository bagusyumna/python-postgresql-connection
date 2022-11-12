import time
import threading
from concurrent.futures import ThreadPoolExecutor
from database import get_connection


def test_function(item):
    print(f'start, id = {threading.get_ident()}')
    conn = get_connection()
    pool = conn.get_pool_conn()
    time.sleep(2)
    conn.put_pool_conn(pool)
    print(f'finished, id = {threading.get_ident()}')


if __name__ == '__main__':
    
    workers = 10
    items = 15

    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(test_function, range(items))

    print('finish all')
