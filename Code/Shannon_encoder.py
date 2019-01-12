# -*- coding: utf-8 -*-
#This file is used to implement Shannon source coding
import math
import os

#count the probability of each character
def creat_prob_list(content):
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

def Shannon_coding_transform(sym,p):
#firstly we need to rearrange the symbol list in descending order
    for j in range(len(sym)):
        for k in range(len(sym)-1-j):
            if p[j]<p[j+k+1]:
                p[j],p[j+k+1]=p[j+k+1],p[j]
                sym[j],sym[j+k+1]=sym[j+k+1],sym[j]
#secondly we need to get the cumulative probability
    p_cum=[]
    p.insert(0,0)
    sum=0
    for i in range(len(p)-1):
        sum=p[i]+sum
        p_cum.append(sum)
#Thirdly we need to get the length of the codeword
    length=[]
    del p[0]

    for k in range(len(p)):
        length.append(math.ceil(math.log(1 / p[k], 2)))
#Lastly we can achieve the Shannon coding
    code=[]
    for i in range(len(sym)):
        t = p_cum[i]
        single_bit_code = ''
        for j in range(length[i]):
            t = t * 2
            t, z = math.modf(t)
            single_bit_code += str(int(z))
        code.append(single_bit_code)
    return sym,code,p

def coding_transform_file(content,sym,code):
    content_list=list(content)
    count=0
    for i in content_list:
        index=sym.index(i)
        content_list[count]=code[index]
        count=count+1
    str=' '.join(content_list)
    coding_file=str.replace(' ','')
    return coding_file


#open up the the preprocessed file
code_path=os.getcwd()           #get current path
dir_name=os.path.dirname(code_path)
file_path=dir_name+"\A Game of Thrones_Preprocess.txt"
try:
    f = open(file_path, 'rb')
except Exception as e:
    print('there is no file named A Game of Thrones')
else:
    content = f.read().decode('utf-8')
    f.close()
sym1,p1=creat_prob_list(content)
sym_new,code,p=Shannon_coding_transform(sym1,p1)
#Calculate average length and coding efficiency
length=0
for i in range(len(sym_new)):
    m=p[i]*len(code[i])
    length=length+m
print('Average Length is: ',length)
H=4.2507
Yita=H/length
print("Coding efficency is: ",Yita)
print("Encoding the file ...")
coding_content=coding_transform_file(content,sym_new,code)
write_path=dir_name+"\Shannon_coding\A Game of Thrones_Shannon_encode.txt"
f1=open(write_path, 'w')
f1.write(coding_content)
f1.close()
print("Encoding file successfully!")