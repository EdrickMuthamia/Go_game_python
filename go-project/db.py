# import psycopg
# from psycopg_pool import ConnectionPool
#
# class PG:
#     def __init__(self):
#         self.credentials = (
#             "host=aws-1-us-east-2.pooler.supabase.com "
#             "dbname=postgres "
#             "user=postgres.mmwdeivfnfjjaxsqcoon "
#             "password=VfJaPAPREfWsdnfN "
#             "port=5432"
#         )
#
#         # You can set min_size, max_size, and timeout as needed
#         self.pool = ConnectionPool(
#             conninfo=self.credentials,
#             min_size=1,
#             max_size=5,
#             timeout=300,
#             open=True
#         )
#
#     def execute(self, query, params=()):
#         with self.pool.connection() as conn:
#             with conn.cursor() as cur:
#                 cur.execute(query, params)
#                 conn.commit()
#
#     def pg_query(self, query, params=()):
#         with self.pool.connection() as conn:
#             with conn.cursor() as cur:
#                 cur.execute(query, params)
#                 result = cur.fetchall()
#                 return result


# db.py
import psycopg
from psycopg_pool import ConnectionPool


class PG:
    def __init__(self):
        # Database connection credentials
        self.credentials = (
            "host=aws-1-us-east-2.pooler.supabase.com "
            "dbname=postgres "
            "user=postgres.mmwdeivfnfjjaxsqcoon "
            "password=VfJaPAPREfWsdnfN "
            "port=5432"
        )

        # Create a pool of reusable connections
        self.pool = ConnectionPool(
            conninfo=self.credentials,
            min_size=1,   # minimum number of connections
            max_size=5,   # maximum number of connections
            timeout=300,  # how long to wait before giving up
            open=True     # open immediately
        )

    # For INSERT, UPDATE, DELETE
    def execute(self, query, params=()):
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                conn.commit()

    # For SELECT (fetching data)
    def pg_query(self, query, params=()):
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                result = cur.fetchall()           # fetch all results
                return result

db = PG()
