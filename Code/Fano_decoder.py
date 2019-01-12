#This file is used to decode fano_coded file to get the original file
import os
code_path=os.getcwd()           #get current path
dir_name=os.path.dirname(code_path)
file_path=dir_name+"\Fano_coding\A Game of Thrones_Fano_encode.txt"
try:
    f = open(file_path, 'rb')#current storing path for "A Game of Thrones.txt"
except Exception as e:
    print('there is no file named A Game of Thrones')
else:
    content = f.read().decode('utf-8')
    f.close()
print("Decoding the file, Please wait...(It takes about half a minute)")
#upload code and corresponding symbol
sym=[' ', 'e', 't', 'a', 'o', 'h', 'n', 'r', 's', 'i', 'd', 'l', 'w', 'u', 'm', 'g', 'y', 'f', 'c', 'b', 'k', 'p', 'v', 'T', 'I', 'S', 'H', 'A', 'L', 'W', 'R', 'B', 'N', 'M', 'J', 'D', 'C', 'Y', 'G', 'E', 'q', 'O', 'K', 'F', 'j', 'P', 'z', 'x', 'V', 'U', 'Q', 'X']
code=['0000', '0001', '0011', '0100', '0101', '0111', '100000', '100001', '100011', '10011', '1010', '1011', '1100000', '1100001', '1100011', '110011', '11010', '11011', '1110000', '1110001', '1110011', '111010', '111011', '111100000', '111100001', '111100011', '11110011', '11110100', '11110101', '11110111', '1111100000', '1111100001', '1111100011', '111110011', '111110100', '111110101', '111110111', '11111100000', '11111100001', '11111100011', '1111110011', '111111010', '111111011', '11111110000', '11111110001', '11111110011', '1111111011', '1111111100', '1111111101', '11111111100', '11111111101', '11111111111']
code_list=list(content)
s=[]
b=''
for i in code_list:
    b+=i
    for k in code:
        if b==k:
            s.append(sym[code.index(b)])
            b=''
write_path=dir_name+"\Fano_coding\A Game of Thrones_Fano_decode.txt"
f1=open(write_path, 'w')
for k in s:
    f1.write(k)
f1.close()
print('Decoding file successfully!')
