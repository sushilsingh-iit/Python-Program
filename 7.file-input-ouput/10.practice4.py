 # waf to find in which line of the file does the word "learning" occur first.

#print-1 if word not found 

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    
    # Using 'with' automatically closes the file even if errors occur
    try:
        with open("/home/rdx/Python-Programs/Python-Program/7.file-input-ouput/practice.txt", "r") as f:
            for line in f:
                # Check if word exists in the current line
                if word in line:
                    print(line_no)
                    return # Exit function immediately once found
                
                line_no += 1
                
        # If the loop finishes without returning, the word wasn't found
        print(-1)
        
    except FileNotFoundError:
        print("File not found. Please check the path.")

# Call the function
check_for_line()