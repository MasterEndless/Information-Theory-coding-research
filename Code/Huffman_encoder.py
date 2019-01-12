import math
import os
class letter_codeword(object):
    def __init__ (self, letter=0, weight=0,codeword=''):
        self.letter = letter
        self.weight = weight
        self.codeword = codeword

class leafnode(object):
    def __init__ (self, letter=0, weight=0, left=None, right=None, ok = 0):
        self.letter = letter
        self.weight = weight
        self.left = left
        self.right = right
        self.ok = ok
    def isleaf(self):
        return True

class internode(object):
    def __init__(self, weight = 0, left = None, right = None,ok = 0):
        self.weight = weight
        self.left = left
        self.right = right
        self.ok = ok
    def isleaf(self):
        return False

def sort(list):
    list = sorted(list, key=lambda x: x.weight)     # sorted from small weight to large
    return list

def get_weight(str):
    letter = []
    weight = []
    leaves = []
    for i in range(len(str)):
        if letter.count(str[i]) == 0:
            letter.append(str[i])
            weight.append(1)
        else:
            position = letter.index(str[i])
            weight[position] = weight[position] + 1
    for pair in zip(letter, weight):
        leaf = leafnode()
        leaf.letter, leaf.weight = pair[0], pair[1]
        leaves.append(leaf)
    return sort(leaves)

def build_hufftree(list):
    while len(list) != 1:
        a, b = list[0], list[1]
        newnode = internode()
        newnode.weight = a.weight + b.weight
        newnode.left, newnode.right = a, b
        list = list[2:]
        list.append(newnode)
        list = sort(list)
    hufftree = list[0]
    return hufftree

def letter_coder(hufftree,codeword):
    if hufftree.isleaf():
        item = letter_codeword()
        #print(hufftree.letter, hufftree.weight, codeword)
        item.letter = hufftree.letter
        item.weight = hufftree.weight
        item.codeword = codeword
        hufftree.ok = 1
        return item
    else:
        if hufftree.left.ok != 1:
            codeword = codeword + '0'
            return letter_coder(hufftree.left, codeword)
        elif hufftree.right.ok != 1:
            codeword = codeword + '1'
            return letter_coder(hufftree.right, codeword)
        else:
            hufftree.ok = 1

def constr_dict(leaves):
    hufftree = build_hufftree(leaves)
    node_num = 2 * len(leaves) - 1
    dict = []
    for i in range(node_num):
        dict.append(letter_coder(hufftree, ''))
    for i in range(len(dict) - 1, -1, -1):
        if dict[i] == None:
            dict.pop(i)
    return sort(dict)

def huff_coder(dict,input_str):
    output = ''
    for i in range(len(input_str)):
        for item in dict:
            if input_str[i] == item.letter:
                output = output + item.codeword
    return output

def huff_decoder(dict, codes):
    codeword = ''
    letters = ''
    for i in range(len(codes)):
        codeword = codeword + codes[i]
        for item in dict:
            if codeword == item.codeword:
                letters = letters + item.letter
                codeword = ''
    return letters

def huff_efficiency(leaves,dict):
    total_weight = 0
    entropy = 0.
    av_len = 0.
    for item in leaves:
        total_weight = total_weight + item.weight
    for item in leaves:
        p = item.weight/total_weight
        entropy = entropy - p * math.log(p,2)
    for item in dict:
        p = item.weight / total_weight
        av_len = av_len + p * len(item.codeword)
    print("Source Entroy =", entropy)
    print("Average Length =", av_len)
    print("Coding Efficiency =", entropy/av_len)

# get the path of preprocess file
dir_name = os.path.dirname(os.getcwd())

# get the leaves (letter - weight)
with open(dir_name + "\\A Game of Thrones_Preprocess.txt","r") as f:
    str = f.read()
leaves = get_weight(str)

# construct dict
dict = constr_dict(leaves)
dict_str = ''
for item in dict:
    dict_str = dict_str + item.letter + ' '
    dict_str = dict_str + item.codeword
    dict_str = dict_str + '\n'

# calculate the coding efficiency
huff_efficiency(leaves,dict)

# write codebook file
print('\nGenerating the codebook ...');
with open("A Game of Thrones_Huffman_codebook.txt", 'w') as f:
    f.write(dict_str)
print('Write successfully as \"A Game of Thrones_Huffman_codebook.txt\"');

# encoding
print('\nGenerating the encode file ...');
codes = huff_coder(dict, str)

# write encode file
with open("A Game of Thrones_Huffman_encode.txt", 'w') as f:
    f.write(codes)
print('Write successfully as \"A Game of Thrones_Huffman_encode.txt\"');