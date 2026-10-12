from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    counts = defaultdict(int)

    for char in s:

        if char in counts:
            counts[char] += 1

        else:
            counts[char] = 1

    return counts

def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    result = defaultdict(list)

    for sublist in nums:
        key = sublist[0]
        values = sublist[1:]

        if key in result:
            result[key].extend(values)
        else:
            result[key] = values

    return result


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
