letter = '''Dear <|Name|>

Hello <|Name|> very are happy to announce that you have been selected in your interview
and we would like to have you in our company

<|Date|>
'''
name = input("Enter the name to be printed on the letter:\n")
date = input("Enter the date to be printed on the letter:\n")
letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)