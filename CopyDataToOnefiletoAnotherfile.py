# 5. Copy Content to Another File
# Write a Python program that reads the content of myfile.txt and copies it into a new file
# called copy.txt. Verify that copy.txt contains the same content as myfile.txt.

with open("myfile.txt","r") as rf:
    content=rf.read()
    with open("copy.txt","w") as wf:
        wf.writelines(content)