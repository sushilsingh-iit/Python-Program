# python can be used to perform operations on file. (read and write data)

# open ,read ,and close file 
# f = open("file_name ", "mode")


# # sammple.txt # r:read mode
# # demo.docx  # w: write mode 

# data = f.read()

# f.close()

f = open("/home/rdx/Python-Programs/Python-Program/7.file-input-ouput/demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()


# data = f.raed() # read entire file 
# data = f.raedline  # read one line at a time 


# character                                # meaning 

#'r'                    open for reading (defult)
#'w'                    open for writing , truncating the file first
#'x'                    create a new file and open it for writing 
#'a'                    open fro writing ,appending to the end of the file if it exists
#'b'                    binary mod e
#'t'                    text mode(defult)
#'+"                    open a disk file for uploading (reading and writing )







