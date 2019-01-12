#This file is used to implement fano encoding

import sys
import os
sys.setrecursionlimit(1000)
def creat_prob_list(content):    #create symbol list and probability list
    dict_sym_count = {}
    total_num=0
    p=[]

    for v in content:
        if v in dict_sym_count:
            dict_sym_count[v] += 1
        elif v not in dict_sym_count:
            dict_sym_count[v] = 1
    for i in dict_sym_count:
        total_num=total_num+dict_sym_count[i]
    for i in dict_sym_count:
        prob=dict_sym_count[i]/total_num
        p.append(prob)
    sym=list(dict_sym_count.keys())
    return sym,p

def arrange_order(sym,p):           ##rearrange the symbol list in descending order and create symbol-probability-code list
    sym_prob_code=[]
    for j in range(len(sym)):
        for k in range(len(sym)-1-j):
            if p[j]<p[j+k+1]:
                p[j],p[j+k+1]=p[j+k+1],p[j]
                sym[j],sym[j+k+1]=sym[j+k+1],sym[j]
    for i in range(len(sym)):
        sym_prob_code.append([sym[i],p[i],''])
    return sym_prob_code


def divide_position(turple):  # find the divide position
    empty_list = []
    for k in range(len(turple)):
        sumA = 0
        sumB = 0
        for i in range(k):
            sumA += turple[i][1]
        for i in range(k, len(turple)):
            sumB += turple[i][1]
        dif = abs(sumA - sumB)
        empty_list.append((k, dif))
    sorted_list = sorted(empty_list, key=lambda dif: dif[1])
    return sorted_list[0][0]

def fano_coding(sym_prob_code,direc):     #Fnao coding process
    if len(sym_prob_code)==1:
        if direc=='left':
            sym_prob_code[0][2]+='0'
        elif direc=='right':
            sym_prob_code[0][2]+='1'
        return
    if len(sym_prob_code)==2:
        sym_prob_code[0][2]+='0'
        sym_prob_code[1][2]+='1'
        return
    index=divide_position(sym_prob_code)
    length=len(sym_prob_code)
    for i in range(index+1):
        sym_prob_code[i][2]+='0'
    for i in range(index+1,len(sym_prob_code)):
        sym_prob_code[i][2]+='1'
    fano_coding(sym_prob_code[0:index+1],'left')
    fano_coding(sym_prob_code[index+1:length],'right')
    return sym_prob_code

def coding_transform_file(content,turple):        #Write coding to the file
    content_list=list(content)
    count=0
    for i in content_list:
        for k in range(len(turple)):
            if i==turple[k][0]:
                content_list[count]=turple[k][2]
        count+=1
    str=' '.join(content_list)
    coding_file=str.replace(' ','')
    return coding_file

code_path=os.getcwd()           #get current path
dir_name=os.path.dirname(code_path)
file_path=dir_name+"\A Game of Thrones_Preprocess.txt"
try:
    f = open(file_path, 'rb')#current storing path for "A Game of Thrones.txt"
except Exception as e:
    print('there is no file named A Game of Thrones')
else:
    content = f.read().decode('utf-8')
    f.close()

sym1,p1=creat_prob_list(content)
sym_prob_code=arrange_order(sym1,p1)
encode_list=fano_coding(sym_prob_code,'left')
#Calculate average length
length=0
for i in range(len(encode_list)):
    m=encode_list[i][1]*(len(encode_list[i][2]))
    length=length+m
print ("Average length is: ",length)
H=4.2507
Yita=H/length
print("Coding efficency is: ",Yita)
print("Encoding the file ...")
write_content=coding_transform_file(content,encode_list)
write_path=dir_name+"\Fano_coding\A Game of Thrones_Fano_encode.txt"
f1=open(write_path, 'w')
f1.write(write_content)
f1.close()
print('Encoding file successfully!')



















