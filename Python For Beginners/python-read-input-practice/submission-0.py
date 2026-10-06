def add_two_numbers() -> int:
    int_input = input()
    string_list = int_input.split(",")

    total = 0
    for num in string_list:
        total += int(num) 
    return total





# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
