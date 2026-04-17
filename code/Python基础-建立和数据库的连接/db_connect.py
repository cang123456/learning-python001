import pymysql
import configparser  # Python标准库，用于读取INI配置文件

# 打开数据库连接
# db = pymysql.connect(host='localhost',
#                      user='root',
#                      password='123456',
#                      database='python'
#                      )



def read_ini():
    config = configparser.ConfigParser()  # 创建配置解析器对象。
    config.read('user.ini', encoding="utf-8")
    host = config.get("mysql", 'host')
    port = config.getint("mysql", 'port')
    user = config.get("mysql", 'user')
    password = config.get("mysql", 'password')
    database = config.get("mysql", 'database')
    return (host,port,user,password,database)

def solve(insert_data):
    # insert_data = ("抖音用户", "192.168.1.1", "测试评论内容", "https://www.douyin.com/user/123")
    # # 使用cursor方法获取操作游标
    # cursor = db.cursor()

    # sql插入语句

    sql = 'insert into douyin_pinlun002(name,ip,text,user_url) values (%s,%s,%s,%s)'


    try:

        host, port, user, password, database = read_ini()
        # 打开数据库连接
        conn = pymysql.connect(
            host=host, user=user, password=password, database=database, port=port
        )
        # 创建游标（执行SQL的核心对象）
        cursor = conn.cursor()
        #执行插入的sql （传入SQL和参数元组）
        cursor.execute(sql,insert_data)
        # 提交
        conn.commit()

    except Exception as e:
        print(e)

    finally:
        # 无论成功/失败，都关闭游标和连接，释放资源
        if cursor:
            cursor.close()
        if conn:
            conn.close()



    # config = configparser.ConfigParser()  # 创建配置解析器对象。
    # config.read('user.ini', encoding="utf-8")
    # host = config.get("mysql", 'host')
    # port = config.getint("mysql", 'port')
    # user = config.get("mysql", 'user')
    # password = config.get("mysql", 'password')
    # database = config.get("mysql", 'database')
    # czl = config.get("mysql1", 'czl')
    # print(host, port, user, password, database, czl, end='\n')