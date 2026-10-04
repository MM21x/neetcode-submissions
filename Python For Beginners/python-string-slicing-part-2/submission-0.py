def first_n_characters(s: str, n: int) -> str: #s= string n = number
    i = len(s) - 1
    return(s[:n])

def last_n_characters(s: str, n: int) -> str:
    i = len(s) -  n
    return(s[i:])


# do not modify below this line
print(first_n_characters("NeetCode", 3))
print(first_n_characters("NeetCode", 4))
print(first_n_characters("NeetCode", 8))

print(last_n_characters("NeetCode", 3))
print(last_n_characters("NeetCode", 4))
print(last_n_characters("NeetCode", 8))
