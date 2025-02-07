#open()---function
# ---------------------------------------
# try:
#     varname=open("File11.txt","r")
#     content = varname.read()  # Read the entire content of the file
#     print("Content in file :",content)  # Display the content
#     varname.close()  # Close the file after reading
# except FileNotFoundError:
#     print("File is not Exists")
    #-------------------------------------------
# else:
#     print("File Opened in read mode Successfully.")
    
# try:
#     var=open("File1.txt","w")
# except FileNotFoundError:
#     print("File is not Exists")
# else:
#     print("File Opened in write mode Successfully.")


# try:
#     var=open("createappendFile.txt","a")
# except FileNotFoundError:
#     print("File is not Exists")
# else:
#     print("File Opened in append mode Successfully.")
#     var.close()


# with open()--------function
# -------------------------
# with open("appendFile.txt","r") as fp:
#     content=fp.read()
#     print("readline the file :",content)
# print("==============================================================")
# with open("appendFile.txt","r") as fp:
#     for line in fp:
#         print("using loops",line)
# print("==============================================================")
# # with open()--------function
# # -------------------------
# with open("appendFile.txt","r") as fp:
#     content=fp.readlines()
#     print("readlines the file :",content)

    
    
# with open("appendFile.txt", "r") as file:
#     part = file.read(10) # Reads the first 10 characters
#     print(part)
#     print(file.readable())
#     print(file.writable())
#     print(file.closed)
#     print(file.name)
#     print(file.mode)
# print(file.closed)


# sno=12
# sname="latha Dande"
# marks=56.65
# with open("writefile.txt","w") as fp:
#     fp.write(str(sno)+"\t")
#     fp.write(sname+"\t")
#     fp.write(str(marks)+"\t")

# sno=int(input("Enter your sno:"))
# sname=input("Enetr your name:")
# marks=float(input("enter your marks:"))
# with open("writelinesfile.txt","w") as fp:
#     fp.writelines(str(sno)+"\t")
#     fp.writelines(sname+"\t")
#     fp.writelines(str(marks)+"\t")

# with open("writefile.txt","r") as rp:
#     var=rp.read()
#     print(var)
    
# print("======================================")
# with open("writefile.txt","r") as rp:
#     var=rp.readlines()
#     # print(var)
#     for record in var:
#         print(record)

# with open("example.txt", "w") as file:
#     lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
#     file.writelines(lines)

with open("example.txt", "w") as file:
    # lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
    line="hi"
    file.write(line)