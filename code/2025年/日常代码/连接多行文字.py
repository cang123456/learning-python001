



# 多行合并，并且去掉末尾的换行符号

def sovle(ans0):
    ans = []
    for line in ans0:
        stripped_line = line.rstrip('\n')
        # if line[len(line)-1] == '\n':
        #     ans.append(line[0:len(line)-2])
        # else:
        ans.append(stripped_line)
    return ans

try:
    with open('1.txt','r',encoding='utf-8') as f:
        ans0 = f.readlines()
    ans = sovle(ans0)
    with open('1.txt','w',encoding='utf-8') as f:
        for line in ans:
            f.write(line)
except FileNotFoundError:
    print("erro1")