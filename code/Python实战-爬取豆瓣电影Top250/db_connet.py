import pymysql
import configparser



def read_ini():
    config = configparser.ConfigParser()
    config.read('user.ini',encoding='utf-8')
    host = config.get("mysql", 'host')
    port = config.getint("mysql", 'port')
    user = config.get("mysql", 'user')
    password = config.get("mysql", 'password')
    database = config.get("mysql", 'database')
    table_name = config.get("mysql", 'table_name')
    return (host, port, user, password, database, table_name)


def solve(inse_data):
    host, port, user, password, database, table_name = read_ini()

    try:

        sql = f'insert into {table_name}(rankings,name,image_url,movie_rating,movie_author,numofeva,movie_lab) values (%s,%s,%s,%s,%s,%s,%s)'
        conn = pymysql.connect(host=host, user=user, password=password, database=database, port=port)

        couser = conn.cursor()
        couser.execute(sql,inse_data)

        # 提交
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()
        if couser:
            couser.close()


# solve((1,'test','test','test','test','test','test'))

























