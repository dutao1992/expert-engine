#-*- coding:utf-8 -*-
from __future__ import division
import math
import numpy as np
import matplotlib.pyplot as plt


def distance(x,y):
    return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)

def cross_point(line1,line2):
    if line1[0] == 'INF' :
        return line1[1],line1[1]*line2[0]+line2[1]
    elif line2[0] == 'INF' :
        return line2[1],line2[1]*line1[0]+line1[1]
    else:
        return (line2[1]-line1[1])/(line1[0]-line2[0]),line1[0]*((line2[1]-line1[1])/(line1[0]-line2[0]))+line1[1]

def Area(p0,p1,p2):
    sum = (p1[0] - p0[0])*(p2[1] - p0[1]) - (p2[0] - p0[0])*(p1[1] - p0[1])
    if sum < 0:
        return -(sum / 2)
    return sum / 2

def gravity_point(poly):

    sumarea = Area(poly[0], poly[1], poly[2])
    sumx = (poly[0][0] + poly[1][0] + poly[2][0]) * Area(poly[0], poly[1], poly[2])
    sumy = (poly[0][1] + poly[1][1] + poly[2][1]) * Area(poly[0], poly[1], poly[2])

    i = 2
    while i<len(poly)-1:
        if Area(poly[0],poly[i],poly[i+1]) > 0:
            sumarea += Area(poly[0],poly[i],poly[i+1])
            sumx += (poly[0][0] + poly[i][0] + poly[i+1][0]) * Area(poly[0], poly[i], poly[i+1])
            sumy += (poly[0][1] + poly[i][1] + poly[i+1][1]) * Area(poly[0], poly[i], poly[i+1])

        elif Area(poly[1], poly[2], poly[3]) == 0:
            sumx += 0
            sumy += 0
        i += 1
    if sumarea != 0:
        return sumx/(3 * sumarea),sumy /(3 * sumarea)


def isInsidePolygon(pt, poly):
    c = False
    i = -1
    l = len(poly)
    j = l - 1
    while i < l-1:
        i += 1
       # print i,poly[i], j,poly[j]
        if ((poly[i][0] <= pt[0] and pt[0] < poly[j][0]) or (poly[j][0] <= pt[0] and pt[0] < poly[i][0])):
            if (pt[1] < (poly[j][1] - poly[i][1]) * (pt[0] - poly[i][0]) / (poly[j][0] - poly[i][0]) + poly[i][1]):
                c = not c
        j = i
    return c


def sum_distance(p0, p1, p2, p3,points):

    if p0[0] - p2[0] != 0 and p1[0] - p3[0] != 0:
        l1 = [(p0[1] - p2[1]) / (p0[0] - p2[0]), p0[1]]
        l2 = [(p1[1] - p3[1]) / (p1[0] - p3[0]), p1[1]]
    elif p0[0] - p2[0] == 0:
        l1 = ['INF',p0[1]]
        l2 = [(p1[1] - p3[1]) / (p1[0] - p3[0]), p1[1]]
    elif p1[0] - p3[0] == 0:
        l1 = [(p0[1] - p2[1]) / (p0[0] - p2[0]), p0[1]]
        l2 = ['INF',p1[1]]

    part_region = {'part1': [(0, 1), cross_point(l2, (0, 1)), cross_point(l1, l2), cross_point(l1, ('INF', 0))],
                   'part2': [cross_point(l1, l2), cross_point(l2, (0, 1)), (1, 1), cross_point(l1, ('INF', 1))],
                   'part3': [(0, 0), cross_point(l1, ('INF', 0)), cross_point(l1, l2), cross_point(l2, (0, 0))],
                   'part4': [cross_point(l2, (0, 0)), cross_point(l1, l2), cross_point(l1, ('INF', 1)), (1, 0)]}
    part_gravity = {}
    part_gravity['p1'] = gravity_point(part_region['part1'])
    part_gravity['p2'] = gravity_point(part_region['part2'])
    part_gravity['p3'] = gravity_point(part_region['part3'])
    part_gravity['p4'] = gravity_point(part_region['part4'])
    sum1, sum2, sum3, sum4 = 0,0,0,0
    for point in points:
        if isInsidePolygon(point, part_region['part1']):
            sum1 += distance(point, part_gravity['p1'])
        elif isInsidePolygon(point, part_region['part2']):
            sum2 += distance(point, part_gravity['p2'])
        elif isInsidePolygon(point, part_region['part3']):
            sum3 += distance(point, part_gravity['p3'])
        else:
            sum4 += distance(point, part_gravity['p4'])
    sum_all = sum1 + sum2 + sum3 + sum4
    return sum_all

if __name__ == '__main__':
    '''
    1.初始两条直线(每条边上选一个点）
    2.求出交点分割出的四个区域和四个区域的重心
    3.点在某个区域内则求它到该区域重心的距离
    4.将所有距离加和保存
    5.下两条直线，如果所有距离加和小于前一步覆盖，大于或等于则不变
    '''
    points = np.random.rand(500,2)
    p0 = [0, 0.5]
    p1 = [0.5, 1]
    p2 = [1, 0.5]
    p3 = [0.5, 0]
    box = {} #保存区域和散点到区域重心距离之和到该字典

    def find():
        x = sum_distance(p0,p1,p2,p3,points)
        p0[1] += 0.01
        p1[0] += 0.01
        p2[1] -= 0.01
        p3[0] -= 0.01
        if p0[1] <= 1:
            box[x] = [p0, p1, p2, p3]
            find()
        return min(box.iteritems(), key=lambda x:x[0])[1]#返回使得散点到区域重心距离之和为最小的区域划分方式

    find()

    fig = plt.figure()
    plt.xlim(0,1)
    plt.ylim(0,1)
    ax = fig.add_subplot(111)
    x = [x[0] for x in points]
    y = [y[1] for y in points]
    ax.scatter(x,y)
    xp = np.linspace(0,1,100)
    ax.plot(xp,(p0[1] - p2[1]) / (p0[0] - p2[0])*xp+p0[1])
    ax.plot(xp,(p1[1] - p3[1]) / (p1[0] - p3[0])*(xp-p1[0])+p1[1])
