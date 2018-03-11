fout = open('index.h', 'w')
text = ["#include <iostream>", "void print_index()", "{",
'''std::cout << "preparing.py generate file index.h" << std::endl;''',
"}"]
for str in text:
    fout.write(str + "\n")
fout.close() 
