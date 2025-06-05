"""
1. Write a function swap_case(sentence) that takes a sentence as input and returns the sentence with swapped case (e.g., uppercase characters become 
lowercase and vice versa). For example, swap_case("Hello World") should return "hELLO wORLD"

2. Write a function count_title_case(sentence) that takes a sentence as input and returns the number of words in title case (first letter of each word capitalized). For example, count_title_case("Python is an Amazing Programming Language") should return 4.
"""

def swap_case(sentence):
    return sentence.swapcase()


def count_title_case(sentence):
    words = sentence.split()
    return sum(1 for word in words if word.istitle())

print(swap_case('hello'))
print(count_title_case("Python is an Amazing Programming Language"))