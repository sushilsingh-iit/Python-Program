# WAF that replace all occurances of "java " with "python" in above file .

with open("/home/rdx/Python-Programs/Python-Program/7.file-input-ouput/practice.txt", "r")as f:
    data = f.read()


new_data = data.replace("java", "python")



with open("/home/rdx/Python-Programs/Python-Program/7.file-input-ouput/practice.txt", "w")as f:
    f.write(new_data)
    print(new_data)

# Question - search if the word "learning exists" in the file or not.
