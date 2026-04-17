add = lambda x,y:x+y

print(add(3,4))

print(add('3','4'))

nums = [1, 2, 3, 4]
nums2 = (1,2,3,4)

sq = lambda x:x**2
# map：将lambda应用到列表每个元素（计算平方）
sq_n1 = list(map(sq,nums))
sq_n2 = list(map(sq,nums2))

print(sq_n1 ,sq_n2)

# filter：过滤出列表中的偶数(lambda 决定
jishu = lambda x: not x%2 == 0
oushu = list(filter(jishu,nums))
oushu2 = list(filter(jishu,nums2))

print(oushu,oushu2,end='\n')









