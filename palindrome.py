# Problem: Check if a string is palindrome

# Approach:
# Compare string with its reverse

def is_palindrome(s):
    return s == s[::-1]

# Example
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False

# Time Complexity: O(n)
# Space Complexity: O(1)