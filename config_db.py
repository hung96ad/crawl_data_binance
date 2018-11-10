try:
    import mysql.connector as mysql
except :
    import MySQLdb  as mysql

def config_db():
    return mysql.connect(user='root', password='your_password',
                            host='your_ip',
                            database='your_db')                        
