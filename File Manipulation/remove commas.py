#!/bin/python3
import subprocess
import sys

file_in = open(sys.argv[1],'r')
file_out = open(sys.argv[2],'w+')

text_in = file_in.read()
text_out = ''
flag = 0
print('Please Wait')
for x in text_in:
    if x == ',':
        text_out+=' '
    elif x ==' ':
        if flag == 0:
            text_out+=''
            flag = 1
        else:
            pass
    else:
        text_out+=x
        flag = 0

file_out.write(text_out)
print('Done!')
