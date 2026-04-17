import pymysql


# 打开数据库连接
# db = pymysql.connect(host='localhost',
#                      user='root',
#                      password='123456',
#                      database='python'
#                      )

def solve(insert_data):
    insert_data = ("抖音用户", "192.168.1.1", "测试评论内容", "https://www.douyin.com/user/123")
    # # 使用cursor方法获取操作游标
    # cursor = db.cursor()

    # sql插入语句

    sql = 'insert into douyin_pinlun001(name,ip,text,user_url) values (%s,%s,%s,%s)'


    try:
        # 打开数据库连接
        conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            database='python'
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


