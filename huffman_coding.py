# Ali Ejlalzadeh
# Huffman Code in python
import sys
import tkinter as tk
from tkinter import filedialog
print(50*'*')
choice = input("Hi. For console enter:1  and for file enter:2\nSo Enter Your Choice : ")

if choice == '1':
    string=input("Enter Your String :")

elif choice=='2' :
    root = tk.Tk()
    file_path = filedialog.askopenfilename()
    with open(file_path,'r') as f :
        string=''.join(f.readlines())
else :
    print("Please Enter Correct input.")
    exit(1)
       
if len(string)==1:
    print('0')
    exit(0)


class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, binString + '0'))
    d.update(huffman_code_tree(r, binString + '1'))
    return d


# Calculating frequency
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)


huffmanCode_dict = huffman_code_tree(nodes[0][0])
print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    if char == ' ':
        temp = 'space'
        print(temp,'   |   ',huffmanCode_dict[char])
    else :
      print(char,'       |   ',huffmanCode_dict[char])

    
huffman_code=''
for c in string:
    huffman_code=huffman_code+huffmanCode_dict[c]

#simple coding calculations
my_set=set()    
for item in string:
    my_set.add(item)
simple_coding_length=(len(bin(len(my_set)))-2)*len(string)


print(f"\nHuffman Code : {huffman_code}\t\tLength : {len(huffman_code)}")
print(f"Simple Coding Length : {simple_coding_length}")
print(f"Difference in bits : {simple_coding_length-len(huffman_code)}")
key=input()

