# Write a program to check if the given strings are anagram or not
# An anagram of a string is another string that contains the same characters, only the order of characters can be different
# For example, “act” and “tac” are anagrams of each other

def anagram(str1: str, str2: str):
    return "String is anagram" if sorted(str1) == sorted(str2) else "String is not anagram"


try:
    string_one = input("Enter the first string: ")
    string_two = input("Enter the second string: ")

    result = anagram(string_one, string_two)
    print(result)

except Exception as ex:
    print(ex)
