# Question - search if the word "learning exists" in the file or not.


with open("/home/rdx/Python-Programs/Python-Program/7.file-input-ouput/practice.txt","r") as f:
    data = f.read()
    word = "learning"
    if (data.find(word) !=1):
        print("found")

    else:
        print("not found ")    



# waf to find in which line of the file does the word "learning" occur first.
#print-1 if word not found 

def check_for_word():
    word = "learning"
    data = True
    line_no = 1
    with open("/home/rdx/Python-Programs/Python-Program/7.file-input-ouput/practice.txt","r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
                return
            line_no += 1 

    return -1 

print(check_for_word())    