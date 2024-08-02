# Write a program to check if the given strings are anagram or not
# An anagram of a string is another string that contains the same characters, only the order of characters can be different
# For example, “act” and “tac” are anagrams of each other

def anagram(str1: str, str2: str):
    # sorted() is used to sort all the character alphabet wise
    return "String is anagram" if sorted(str1) == sorted(str2) else "String is not anagram"


try:
    # Input keyword is used to take number from command line (Default type String)
    string_one = input("Enter the first string: ")
    string_two = input("Enter the second string: ")

    result = anagram(string_one, string_two)
    print(result)

# If any exception is raised in above try block then the error will be caught below and printed out
except Exception as ex:
    print(ex)
