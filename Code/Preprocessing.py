# -*- coding: utf-8 -*-
#This file is used to delete redundant symbols of the novels
import re
import os
code_path=os.getcwd()  #get file path
file_path=os.path.join(code_path,"A Game of Thrones.txt")
try:            #open file and upload data
    f = open(file_path, 'rb')#current storing path for "A Game of Thrones.txt"
except Exception as e:
    print('there is no file named A Game of Thrones')
else:
    print('open file successfully')
    content = f.read().decode('utf-8')
    f.close()

word = re.findall('[a-zA-Z]+', content)         #find all the word and connect it to become a string
content_list = []
for i in word:
    content_list.append(i)
content_del_sym=" ".join(content_list)
write_path=code_path+'\A Game of Thrones_Preprocess.txt'
fh = open(write_path,'w')
fh.write(content_del_sym)
fh.close()
print('write file successfully!')
