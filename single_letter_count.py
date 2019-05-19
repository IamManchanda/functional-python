""" Python Functions """

def single_letter_count(string, letter):
    lower_string = string.lower()
    lower_letter = letter.lower()
    return lower_string.count(lower_letter)

print( single_letter_count("Hello World", "h") )
print( single_letter_count("Hello World", "z") )
print( single_letter_count("Hello World", "l") )

