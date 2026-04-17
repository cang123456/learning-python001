def print_person_info(name, age=18, *hobbies, **other_info):
    """打印个人信息"""
    print(f"姓名：{name}，年龄：{age}")
    print(f"爱好：{hobbies}")  # hobbies是元组
    print(f"其他信息：{other_info}")  # other_info是字典

# 调用
print_person_info("李四", 20, "看书", "跑步", city="北京", job="程序员")
"""
输出：
姓名：李四，年龄：20
爱好：('看书', '跑步')
其他信息：{'city': '北京', 'job': '程序员'}
"""


def calculate(a, b):
    """返回两数的和与积"""
    sum_val = a + b
    product_val = a * b
    return sum_val, product_val  # 等价于 return (sum_val, product_val)

# 接收多个返回值
sum_res1, product_res1 = calculate(3, 3)
print(sum_res1)      # 输出：9
print(product_res1)  # 输出：20

# 全局变量
global_num = 10


def test_scope():
    # 局部变量
    local_num = 20
    # 读取全局变量
    print(global_num)  # 输出：10

    # 修改全局变量（需用global声明）
    global global_num
    global_num = 100

    # 嵌套函数+nonlocal
    def inner_func():
        nonlocal local_num  # 声明修改外层函数的局部变量
        local_num = 200

    inner_func()
    print(local_num)  # 输出：200


test_scope()
print(global_num)  # 输出：100



# lambda匿名函数（计算两数之和）
add = lambda x, y: x + y
print(add(3, 4))  # 输出：7



