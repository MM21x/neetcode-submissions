from typing import List

def read_integers() -> List[int]:
    number_string = input()
    string_list = number_string.split(",")
    result = []
    for num in string_list:
        result.append(int(num)) 
    return(result)

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
