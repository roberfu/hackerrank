def is_palindrome(str):
    if len(str) <= 1:
        return True
    if str[0] == str[len(str)-1]:
        return is_palindrome(str[1:-1])
    else:
        return False

print(is_palindrome("anna")) # True