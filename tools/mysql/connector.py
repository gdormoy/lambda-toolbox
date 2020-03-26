import sys
import logging

import MySQLdb

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def create_connection(hostname, username, password, database):
    try:
        db = MySQLdb.connect(hostname, user=username,
                               passwd=password, db=database, connect_timeout=10)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()

    logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
    return db

