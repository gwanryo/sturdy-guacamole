from database.connection import Connection
import psycopg2
import logging

# https://www.reddit.com/r/flask/comments/icnxpa/correct_way_to_psycopg2_connection_pooling_in/

logger = logging.getLogger(__name__)

class Database:
    connection = None

    def __init__(self, conn):
        self.connection = Connection(conn)

    def get(self):
        return self.connection.pool.getconn()

    def put(self, connection):
        self.connection.pool.putconn(connection)

class Query:
    pool = None
    connection = None
    cursor = None

    def __init__(self, pool):
        self.pool = pool
        self.connection = self.pool.get()
        self.cursor = self.connection.cursor()

    def execute(self, query, parameters=None):
        try:
            self.cursor.execute(query, parameters)
        except (psycopg2.NotSupportedError, psycopg2.ProgrammingError, psycopg2.DataError, psycopg2.IntegrityError, psycopg2.InternalError, psycopg2.OperationalError, psycopg2.DatabaseError, Exception) as e:
            logger.error("Error while query!")
            raise Exception

    def row(self):
        return self.cursor.rowcount

    def fetch(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.pool.put(self.connection)