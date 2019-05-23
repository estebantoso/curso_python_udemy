def is_palindrome(param):
    is_equal = True
    param = param.replace(" ", "")
    for i in range(int(len(param)/2)):
        if param[i] != param[len(param)-1-i]:
            is_equal = False    
    return is_equal

print(is_palindrome("ab   a"))