# -*- coding:utf-8 -*-

list_letter = ['a','b','c','d','e','f','g']

def count_max(nums):
    #设置出度、入度和度列表
    list_count_in = []
    list_count_out = []
    list_count = []
    
    #初始化列表
    for i in range(len(list_letter)):
        list_count_in.append(0)
        list_count_out.append(0)
        
    #生成入度列表
    for i in range(len(list_letter)):
        for j in range(len(nums)):
            if nums[j][1] == list_letter[i]:
                list_count_in[i] +=1
                
    #生成出度列表    
    for i in range(len(list_letter)):
        for j in range(len(nums)):
            if nums[j][0] == list_letter[i]:
                list_count_out[i] +=1

    #生成度列表并打印
    for i in range(len(list_letter)):
        list_count.append(list_count_in[i]-list_count_out[i])
        print(list_letter[i],"的度为",list_count[i])

    position = [0]#初始化位置列表
    max_list = [list_count[0]]#初始化最大度列表
    new_list_count = list_count[1:]#防止出现两次'a'，因此遍历生成一个除掉‘a'的度的列表

    for x in range(len(new_list_count)):
        if new_list_count[x] > max_list[-1]:#如果新元素的度大于之前元素最大的度
            max_list =[]#清空最大度列表
            position = []#清空位置列表
            max_list.append(new_list_count[x])#添加新元素的度
            position.append(x+1)#添加新元素位置

        elif new_list_count[x] == max_list[-1]:#如果新元素的度等于之前元素最大的度
            max_list.append(new_list_count[x])#添加新元素的度
            position.append(x+1)#添加新元素的度

    #打印最大度元素及其值
    for pos in range(len(position)):
        print(list_letter[position[pos]],end = ' ')
    print("的度最大，为",max_list[0])


nums = [['a','b'],['a','c'],['a','f'],['b','d'],['c','b'],['c','e'],['c','f'],['d','c'],['d','a'],['d','g'],['e','b'],['e','d'],['f','b'],['f','e'],['g','d']]
count_max(nums)
