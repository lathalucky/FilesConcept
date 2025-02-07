# 1. Create and Write to a File
# Write a Python program that creates a new text file called myfile.txt. Write the following
# lines into the file:
# Hello, this is a file handling assignment.
# Python makes it easy to work with files.
# After writing, close the file.

file=open("myfile.txt","w")
lines=file.writelines("Hello, this is a file handling assignment.\n""Python makes it easy to work with files.""\nAfter writing, close the file.\n")
file.close()