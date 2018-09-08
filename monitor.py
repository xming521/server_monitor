# Windows
import os
import psutil as p
import time



process_list={}
with open('../process.conf','r',encoding='UTF-8') as f:
    for line in f:
        xxlist=line.split('|')
        xxlist[1]=eval(xxlist[1])
        process_list[xxlist[0]]=xxlist[1]


print(process_list)


result_process={}
for i in process_list:
    try:
        process=p.Process(process_list[i])
        result_process[i]=True
    except p.NoSuchProcess:
        result_process[i]=False


    print(process.name(),process.exe(),process.status())



