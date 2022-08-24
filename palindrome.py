def palindrome(name):
    name = name.casefold()
    if name == name[::-1]:
        return True
    else:
        return False


print(palindrome("kajak"))