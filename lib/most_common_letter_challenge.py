
#? Original Function to debug
# def get_most_common_letter(text):
#     counter = {}
#     for char in text:
#         counter[char] = counter.get(char, 0) + 1
#     letter = sorted(counter.items(), key=lambda item: item[1])[0][1]
#     return letter


# print(f"""
# Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
# Expected: o
# Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
# """)


#? Debugged Function 

def get_most_common_letter(text):
    counter = {}
    #Above we create an emtpy dictionary called counter
    for char in text:
    #Above we loop through each character in text (the argument for the function)
        counter[char] = counter.get(char, 0) + 1
        
        #print(f"The key value pair added is {char}: {counter.get(char, 0) + 1}")
    #print(counter)
    letter = sorted(counter.items(), key=lambda item: item[1])[0][1]
    #print(letter)
    #print(type(letter))
    print(sorted(counter.items(), key=lambda item: item[1]))
    sorted_list = (sorted(counter.items(), key=lambda item: item[1]))
    
    
    #need to remove pairs where the key is not a letter 
    new_list = []
    for pair in sorted_list:
        print(pair)
        if pair[0].isalpha():
            new_list.append(pair)
    
    print(new_list)
    
    #then access the last pair and return the key. 
    
    #sorted()[0][1]
    return new_list[-1][0]


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")

