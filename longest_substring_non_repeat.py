# Find the Longest Substring Without Repeating Characters:
# Write a Python function to find the length of the longest substring without repeating characters.


def longest_non_repeat_substring(string: str):
    str_index = {}
    start = 0
    max_length = 0

    for end in range(len(string)):
        if string[end] in str_index:
            start = max(start, str_index[string[end]] + 1)

        str_index[string[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length


try:
    # Input keyword is used to take number from command line (Default type String)
    inp_string = input("Enter the string: ")

    # Passing the above two input as parameter in the below function
    result = longest_non_repeat_substring(inp_string)
    print(result)

except Exception as ex:
    print(ex)