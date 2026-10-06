def divide_numbers(a: str, b: str) -> None:
    try:
        string_int1 = int(a)
        string_int2 = int(b)
        result = string_int1 / string_int2
        print(result)
    except Exception as error:
        print("An error occurred:", error)



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
