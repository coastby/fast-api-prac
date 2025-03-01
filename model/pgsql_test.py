import psycopg as pg
import psycopg_pool as pg_pool
from config import config

pool_default = pg_pool.ConnectionPool(
    config.PGSQL_TEST_DATABASE_STRING + " options='-c search_path=\"test-db\"'",
    min_size=config.PGSQL_TEST_POOL_MIN_SIZE,
    max_size=config.PGSQL_TEST_POOL_MAX_SIZE,
    max_idle=config.PGSQL_TEST_POOL_MAX_IDLE
)

def list_admin():
    with pool_default.connection() as conn:
        cursor = conn.cursor(row_factory=pg.rows.dict_row)
        try: 
          results = cursor.execute("SELECT * FROM admin").fetchall()
        except Exception as e:
          print(e)
          results = False
        return results