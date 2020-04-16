import sys
import logging

import pymysql.cursors

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def create_connection(hostname, username, password, database, port=3306):
    try:
        db = pymysql.connect(hostname, user=username,
                               passwd=password, db=database, connect_timeout=10, port=port)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()

    logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
    return db