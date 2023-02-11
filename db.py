import pymysql

hostname = '127.0.0.1'
username = 'root'
pwd = 'r@@t'
dbname = 'vulnerability_db'
conn = pymysql.connect(host = hostname, user = username, passwd = pwd, db = dbname, port=3307)