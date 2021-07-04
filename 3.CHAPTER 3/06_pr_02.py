letter= ''' Dear <Name>
           You are Selected
           Date:<Date>'''
name=input("Enter your name\n")
Date=input("Enter Date\n")
letter=letter.replace("<Name>",name)
letter=letter.replace("<Date>",Date)
print(letter)
