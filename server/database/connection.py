import psycopg2
import psycopg2.pool, psycopg2.extras
import logging

# https://www.reddit.com/r/flask/comments/icnxpa/correct_way_to_psycopg2_connection_pooling_in/

logger = logging.getLogger(__name__)

class Connection:
    pool = None

    def __init__(self, conn):
        self.name = conn['DB_NAME']
        self.user = conn['DB_USER']
        self.password = conn['DB_PASS']
        self.host = conn['DB_HOST']
        self.port = conn['DB_PORT']
        self.min = conn['DB_CONN_MIN']
        self.max = conn['DB_CONN_MAX']
        self.connect()

    def connect(self):
        try:
            self.pool = psycopg2.pool.ThreadedConnectionPool(
                minconn=self.min,
                maxconn=self.max,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.name,
                cursor_factory=psycopg2.extras.DictCursor
            )
            self.pool.autocommit = True
        except (psycopg2.NotSupportedError, psycopg2.ProgrammingError, psycopg2.DataError, psycopg2.IntegrityError, psycopg2.InternalError, psycopg2.OperationalError, psycopg2.DatabaseError, Exception) as e:
            logger.error("Error while create connection pool!")
            raise Exception
        else:
            logger.warning('Successfully created database pool!')