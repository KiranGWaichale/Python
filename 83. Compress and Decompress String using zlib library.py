# 83. Please write a program to compress and decompress the string \"hello world!hello world!hello world!hello world!

import zlib

# string = 'hello world!hello world!hello world!hello world!'
string = input("Enter a String : ")
compressed_string = zlib.compress(bytes(string, 'utf-8'))

print(f"Compressed String is : {compressed_string}")
print(f"Decompressed String is : {zlib.decompress(compressed_string)}")