#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
ROT13是它自己本身的逆反；要还原ROT13，套用加密同样的演算法即可得，同样的操作可用再加密与解密。
'''

__author__ = 'GQ'

import string
alp = string.ascii_letters

pwd_before = 'Anything that is not contained in braces is considered literal text, which is copied unchanged to the output.' \
             ' If you need to include a brace character in the literal text, it can be escaped by doubling: {{ and }}.'
pwd_after = ''

pwd_before1='Nalguvat gung vf abg pbagnvarq va oenprf vf pbafvqrerq yvgreny grkg, juvpu vf pbcvrq hapunatrq gb gur bhgchg. ' \
            'Vs lbh arrq gb vapyhqr n oenpr punenpgre va gur yvgreny grkg, vg pna or rfpncrq ol qbhoyvat: {{ naq }}.'

# rot13加密，方法一：
for ch in pwd_before:
    if ch in alp:
        if 'a' <= ch <= 'z':
            pwd_after += chr((ord(ch)-ord('a')+13)%26+ord('a'))
        else:
            pwd_after += chr((ord(ch)-ord('A')+13)%26+ord('A'))
    else:
        pwd_after += ch

# rot13加密，方法二：
def rot13(s, OffSet=13):
     def encodeCh(ch):
         f = lambda x: chr((ord(ch)-x+OffSet) % 26 + x)
         return f(97) if ch.islower() else (f(65) if ch.isupper() else ch)
     return ''.join(encodeCh(c) for c in s)

# rot13加密，方法三：
def rot13_2(s, offSet=13):
    d = {chr(i+c): chr((i+offSet) % 26 + c) for i in range(26) for c in (65, 97)}
    return ''.join([d.get(c, c) for c in s])

print(pwd_before)
print(pwd_after)
print(rot13_2(pwd_before1))
print(rot13(pwd_before))