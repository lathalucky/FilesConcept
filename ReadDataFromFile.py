# 2. Read and Display File Content
# Write a Python program to read the contents of myfile.txt (created in the previous
# question) and print it to the console.
with open("myfile.txt","r") as rf:
    content=rf.read()
    print(content)
