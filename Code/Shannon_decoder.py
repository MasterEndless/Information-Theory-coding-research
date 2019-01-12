#This file is used to decode the shannon-coded file to get the original file
import os
code_path=os.getcwd()           #get current path
dir_name=os.path.dirname(code_path)
file_path=dir_name+"\Shannon_coding\A Game of Thrones_Shannon_encode.txt"
try:
    f = open(file_path, 'rb')
except Exception as e:
    print('there is no file named A Game of Thrones')
else:
    content = f.read().decode('utf-8')
    f.close()
print("Decoding the file, Please wait...(It takes about half a minute)")
#upload code and corresponding symbol
sym=[' ', 'e', 't', 'a', 'o', 'h', 'n', 'r', 's', 'i', 'd', 'l', 'w', 'u', 'm', 'g', 'y', 'f', 'c', 'b', 'k', 'p', 'v', 'T', 'I', 'S', 'H', 'A', 'L', 'W', 'R', 'B', 'N', 'M', 'J', 'D', 'C', 'Y', 'G', 'E', 'q', 'O', 'K', 'F', 'j', 'P', 'z', 'x', 'V', 'U', 'Q', 'X']
code=['000', '0011', '0100', '0101', '01101', '01111', '10001', '10010', '10100', '10110', '10111', '11000', '110011', '110101', '110110', '110111', '111000', '111001', '1110101', '1110111', '1111000', '1111001', '11110101', '11110111', '111110000', '111110010', '111110100', '1111101010', '1111101100', '1111101110', '1111110000', '1111110001', '1111110011', '1111110100', '1111110101', '1111110110', '11111110000', '11111110010', '11111110011', '11111110101', '11111110110', '11111110111', '11111111001', '11111111010', '11111111011', '11111111100', '111111111010', '111111111100', '111111111101', '11111111111100', '11111111111110', '111111111111111110']
code_list=list(content)
s=[]
b=''
for i in code_list:
    b+=i
    for k in code:
        if b==k:
            s.append(sym[code.index(b)])
            b=''
write_path=dir_name+"\Shannon_coding\A Game of Thrones_Shannon_decode.txt"
f1=open(write_path, 'w')
for k in s:
    f1.write(k)
f1.close()
print('Decoding file successfully!')




