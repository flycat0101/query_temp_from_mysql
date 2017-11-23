import sys
import logging
import pymysql

DB_HOST = "greengrass.co4tctnwmzmy.us-west-2.rds.amazonaws.com"
DB_USERNAME = "root"
DB_PASSWORD = "PdXnW947JGYVWxDbXbn2BMpNWihHmcSr"
DB_DATABASE = "greengrass"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
def message_handler(event, context):
    try:
        conn = pymysql.connect(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_DATABASE, connect_timeout=5)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()

    sql = "select * from data ORDER BY id desc limit 1"
    cur = conn.cursor()
    cur.execute(sql)  
    
    row = cur.fetchone()
    rows = str(row)
    rows = rows.strip('\n')
    rows = rows.split(",")
    temp = rows[1]
    temp = temp.split("L")
    temp = int(temp[0]) / 10.0
    conn.close()

    return "%.1f" %(temp)
