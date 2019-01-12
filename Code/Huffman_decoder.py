class letter_codeword(object):
    def __init__ (self, letter='',codeword=''):
        self.letter = letter
        self.codeword = codeword

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

# get the dict file
with open("A Game of Thrones_Huffman_codebook.txt","r") as f:
    list = f.readlines()

# get the dictionary
dict = []
letter = ''
codeword = ''
for line in list:
    item = letter_codeword()
    item.letter = line[0]
    item.codeword = line[2:-1]
    dict.append(item)

# read the encode file
with open("A Game of Thrones_Huffman_encode.txt","r") as f:
    str = f.read()

# decoding
print('\nGenerating the decode file ...');
letters = huff_decoder(dict, str)

# write the decode file
with open("A Game of Thrones_Huffman_decode.txt", 'w') as f:
    f.write(letters)
print('Write successfully as \"A Game of Thrones_Huffman_decode.txt\"');