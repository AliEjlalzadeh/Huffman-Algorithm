# Ali Ejlalzadeh
# Huffman Decoding in python
print(50*'*')
print("For Decoding Please First Do Coding For Generating Huffman Tree ")
string=input("Enter your string :")
code = input("Enter Your Huffman Code :")


# Creating tree nodes
class NodeTree(object):
    
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

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
    
node = nodes[0][0]
decoded_str=''

for c in code:
    if c=='1':
        node = node.right
        if type(node)==str:
            decoded_str+=node
            node=nodes[0][0]
    elif c=='0':
        node = node.left
        if type(node)==str:
            decoded_str+=node
            node=nodes[0][0]

print(f"Decoded string is : {decoded_str}")
key=input()




