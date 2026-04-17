import psutil  # 1. 导入psutil库：Python的系统监控工具库，能获取进程、网络、CPU、内存等系统信息，这里核心用来获取网络连接和进程详情
import socket  # 2. 导入socket库：用于网络编程的基础库（注：这段代码里未实际使用该库的功能，可能是预留/误导入）
import datetime



blackname = ['weixin.exe']


# 核心代码总结

# psutil.net_connections()获取所有TCP/IP（IPv4/IPv6）类型的网络连接
# for conn in psutil.net_connections(kind='inet'):
# conn是单个连接对象，包含该连接的所有属性（PID、地址、状态等）



def wirte_log(s):
    try:
        with open(f'daylog/{datetime.date.today()}_log.txt', 'a+', encoding='utf-8') as f:
            f.write(s + '\n')
    except Exception as e:
        print(e)


# 3. 定义函数：封装获取网络连接信息的逻辑，函数名get_network_connections（获取网络连接）
def get_network_connections():
    # 4. 打印提示信息：告知用户程序正在执行获取操作，提升交互体验
    print('正在获取网络连接信息...')
    # 5. 打印表头：用f-string格式化字符串，<数字表示「左对齐+指定宽度」，让输出成规整的表格形式
    #    表头列：进程名（占25字符）、PID（占8字符）、本地地址（22）、远程地址（22）、状态（15）、进程路径
    s1 = f'{"进程名":<25} {"PID":<8} {"本地地址":<22} {"远程地址":<22} {"状态":<15} {"进程路径"}'
    print(s1)
    wirte_log(s1)
    # 6. 打印分隔线：120个连字符，分隔表头和后续的连接数据，让输出更易读
    print('-' * 120)

    # 7. 遍历网络连接：psutil.net_connections(kind='inet')获取所有TCP/IP（IPv4/IPv6）类型的网络连接
    #    kind='inet'排除了UNIX域套接字等非网络连接，conn是单个连接对象，包含该连接的所有属性（PID、地址、状态等）
    for conn in psutil.net_connections():
        # 8. 异常捕获开始：获取进程信息时可能遇到「进程已结束、权限不足、僵尸进程」等问题，try-except避免程序崩溃
        try:
            # 9. 注释：说明后续代码的作用（获取进程信息）
            # 获取进程信息
            # 10. 创建Process对象：根据连接的PID（进程ID），获取对应的进程对象，后续通过该对象拿进程详情
            proc = psutil.Process(conn.pid)
            # 11. 获取进程名：比如chrome.exe、python.exe、nginx.exe等
            proc_name = proc.name().lower()
            if proc_name in blackname:
                proc.kill()
            # 12. 获取进程路径：进程可执行文件的完整路径，比如C:\Python310\python.exe、/usr/bin/ssh等
            proc_path = proc.exe()

            # 13. 注释：说明后续代码的作用（格式化本地地址）
            # 格式化本地地址
            # 14. 三元表达式：如果conn.laddr（本地地址对象）存在，格式为「IP:端口」；否则显示N/A（无可用地址）
            local_addr = f'{conn.laddr.ip}:{conn.laddr.port}' if conn.laddr else 'N/A'

            # 15. 注释：说明后续代码的作用（格式化远程地址）
            # 格式化远程地址
            # 16. 同本地地址逻辑：远程地址存在则格式为「IP:端口」，否则N/A
            remote_addr = f'{conn.raddr.ip}:{conn.raddr.port}' if conn.raddr else 'N/A'


            # 局域网
            # 127.         本机
            # 10 x x x
            # 192 168 x x
            # 172.16-31.x

            now_ip = conn.raddr.ip.split('.')
            if not (now_ip[0] == '10' or now_ip[0] == '127' or
                (now_ip[0] == '192' and now_ip[1] == '168') or
                (now_ip[0] == '172' and int(now_ip[2]) >= 16 and int(now_ip[2]) <= 31)
            ):
                # 17. 打印单条连接数据：和表头对齐方式一致，输出该连接对应的所有信息
                s2 = f'{proc_name:<25} {conn.pid:<8} {local_addr:<22} {remote_addr:<22} {conn.status:<15} {proc_path}'
                print(s2)
                wirte_log(s2)
            # 18. 捕获特定异常：psutil.NoSuchProcess（PID对应的进程已结束）、AccessDenied（权限不足，无法读取进程信息）、ZombieProcess（僵尸进程）
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # 19. 注释：说明异常处理逻辑（跳过无法获取信息的进程）
            # 如果无法访问进程信息，跳过该进程
            # 20. 跳过当前循环：不打印该连接的信息，直接处理下一个连接
            continue



if __name__ == '__main__':
    # 21. 调用函数：执行整个获取并打印网络连接信息的逻辑
    get_network_connections()