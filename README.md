# Virustotal_Hash_Converter
Virustotal_Hash_Converter (Convert Hashes to SHA  1)

Create a file name hash_input.txt and place your hashes in the file

Usage:
python Hash_Converter_SHA1.py

Example:         
root@Kali:~/Desktop/CTF Stuff# cat hash_input.txt 
0c7652ae9d73e4760e790d57eac5f8d4e31db7fa0e1124aa0d2bd8b24cbdbe7a

root@Kali:~/Desktop/CTF Stuff# python Hash_Converter_SHA1.py 
Checking hash 0c7652ae9d73e4760e790d57eac5f8d4e31db7fa0e1124aa0d2bd8b24cbdbe7a

root@Kali:~/Desktop/CTF Stuff# cat hash_output.txt 
Hash detected 
678bd8c1d0ad249d55872687cd946f8f146897ec
