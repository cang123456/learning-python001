import os
import time

import psutil




def not_local_addr(conn):
    egip = conn.raddr.ip.split('.')
    ip1,ip2 = egip[0],egip[1]
    if not (ip1 == '10' or ip1 == '127' or
            (ip1 == '192' and ip2 == '168') or
            (ip1 == '172' and int(ip2) >= 16 and int(ip2) <= 31) ):
        return True
    else:
        return False


def read_greenip():
    greenip = []
    with open('green_ip.txt','r',encoding='utf-8') as f:
        for line in f:
            # yield line.strip()
            greenip.append(line.strip())
    return greenip
greenip = read_greenip()

def wirte_greenip(ip):
    with open('green_ip.txt','a+',encoding='utf-8') as f:
        f.write(ip+'\n')

bname = []
# 'weixin.exe','todesk.exe','msedge.exe '

def killpro(pid):
    try:
        psutil.Process(pid).kill()
    except Exception as e:
        print("dsb 出错了" + e)


while 1:
    for conn in psutil.net_connections():                  # 拿到所有的连接的进程
        # print(conn)
        if conn.status == 'ESTABLISHED' and conn.raddr:
            egip = conn.raddr.ip
            egname = psutil.Process(conn.pid).name()
        else:
            continue
        # 判断是否是局域网ip
        if not_local_addr(conn):
            print(f"{egname:<40}{egip:<10}")
            # wirte_greenip(egip)                         # 写入白名单

        # 判断是否是白名单已知ip
        if egip in greenip:
            os.system(f"start cmd /k echo 【发现恶意进程】{egname}【来自】{egip}【已终止】")
            killpro(conn.pid)



        if egname.lower() in bname:                     # 杀掉黑名单进程
            killpro(conn.pid)


    print("="*90)
    time.sleep(10)
















