num = int(input("Enter your number: "))

table = [num*i for i in range(1,11)]
print(table)

with open("Table.txt","a") as f:
    f.write(str(table))
    f.write(str("\n"))