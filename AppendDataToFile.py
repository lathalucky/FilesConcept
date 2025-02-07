# 3. Append Data to an Existing File
# Modify myfile.txt by appending the following new line to it:
# This is an appended line.
# Then, read and display the updated content of the file.

with open("myfile.txt","a") as mf:
    modified_content=mf.writelines("This is an appended line.""\nThen, read and display the updated content of the file.")
