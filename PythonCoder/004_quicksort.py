#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'GQ'

def qsort(L):
     if len(L)<=1:return L
     return qsort([left for left in L[1:] if left<L[0]])+ L[0:1] + qsort([right for right in L[1:] if right>=L[0]])

L=[5,4,3,5.5,6,7,2,1,9,10,8]
l=qsort(L)
print(l)