#-*- coding:utf-8 -*-
from __future__ import division
import math

def distance(x,y):
    return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)

def cross_point(l1,l2):
    if l1[0] == 'INF' :
        return l1[1],l1[1]*l2[0]+l2[1]
    elif l2[0] == 'INF' :
        return l2[1],l2[1]*l1[0]+l1[1]
    else:
        return (l2[1]-l1[1])/(l1[0]-l2[0]),l1[0]*((l2[1]-l1[1])/(l1[0]-l2[0]))+l1[1]

def Area(p0,p1,p2):
    sum = (p1[0] - p0[0])*(p2[1] - p0[1]) - (p2[0] - p0[0])*(p1[1] - p0[1]);
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

if __name__ == '__main__':
    '''
    1.初始两条直线
    2.求出交点分割出的四个区域和四个区域的重心
    3.点在某个区域内则求它到该区域重心的距离
    4.将所有距离加和保存
    5.下两条直线，如果所有距离加和小于前一步覆盖，大于或等于则不变
    '''