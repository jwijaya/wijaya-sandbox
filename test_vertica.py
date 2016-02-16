#!/cygdrive/c/Python27/python

"""Summarize metrics for Bash games in summary tables

Usage:
    bash_summarization.py (--username=<username> --password=<password>) [options]
    bash_summarization.py (-h | --help)
Options:
    -h --help                  Show this help message
    --username=<username>      Database connection username
    --password=<password>      Database connection password
    --host=<host>              Database host name or IP address [default: vertica.gsngames.com]
    --port=<port>              Database port [default: 5433]
    --database=<database>      Database name [default: db]
    --start-date=<start_date>  Summarize data on and after this date
                               (YYYY-MM-DD) instead of from the last date
                               (queried from each summary table)
"""

from datetime import datetime
from docopt import docopt
import vertica_python

#import pandas as pd
#import pandas.io.sql
#from pyodbc_helpers import insertKeyedRows
#from task_runner import TaskRunner

#import sys
#sys.path.append('../gsndata')
#from db_tools import get_connection


def main():
    args = docopt(__doc__)
    start_date = args.get('--start-date')
    print('start_date: {}'.format(start_date))

    conn_info = {'host': args.get('--host'),
                 'port': int(args.get('--port')),
                 'user': args.get('--username'),
                 'password': args.get('--password'),
                 'database': args.get('--database'),
                 'read_timeout': 3600} # 1 hour timeout on queries
    print(conn_info)

    with vertica_python.connect(**conn_info) as conn:
        cur = conn.cursor()
        cur.execute("SELECT SYSDATE")
        for row in cur.iterate():
            print(row)


if __name__ == '__main__':
    main()
