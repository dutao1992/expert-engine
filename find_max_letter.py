#二维数组
nums = [['a','b'],['a','c'],['a','c'],['c','a'],['d','a'],['d','b']]

#初始化
count_a,count_b,count_c,count_d = 0,0,0,0

#计算字母在数组第一列中出现的次数
for i in range(len(nums)):
	if nums[i][0] == 'a':
		count_a += 1
	elif nums[i][0] == 'b':
		count_b += 1
	elif nums[i][0] == 'c':
		count_c += 1
	elif nums[i][0] == 'd':
		count_d += 1
print(count_a,count_b,count_c,count_d)

#设置两个列表，一个记录次数，一个记录字母
matrix1 = [count_b,count_c,count_d]
matrix2 = ['a','b','c','d']

#设置一个列表来记录最大次数出现的位置
judge = [0]

#设置一个列表存放最大次数
max_stack = [count_a]
for x in range(len(matrix1)):
    if matrix1[x] > max_stack[-1]:
        max_stack =[]
        max_stack.append(matrix1[x])#如果新的数字大于之前的，清空列表并添加新数字
        judge = []
        judge.append(x+1)#记录新数字在matrix2中的位置
        
    elif matrix1[x] == max_stack[-1]:
        max_stack.append(matrix1[x])#如果新的数字等于之前的最大，添加新数字
        judge.append(x+1)#记录新数字在matrix2中的位置


#打印最多次数列表
print(max_stack)

#打印最多出现次数对应的字母
for i in range(len(judge)):
    print(matrix2[judge[i]])
