""" Python Functions """

def is_palindrome(string):
    return string == string[::-1]

print( is_palindrome("testing") )
print( is_palindrome("tacocat") )
print( is_palindrome("hannah") )
print( is_palindrome("robert") )
print( is_palindrome("amanaplanacanalpanama") )
