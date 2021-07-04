mydict ={
    "vastha":"bag",
    "rumal":"hanki",
    "ghadi":"car"
}
print("Option are" , mydict.keys())
a=input("Enter your item\n")
# print("The meaning of your word", mydict[a])ru
print("The meaning of your word", mydict.get(a))