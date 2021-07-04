# write by jaster
sub1=int(input("Enter your marks sub 1:  "))
sub2=int(input("Enter your marks sub 2:  "))
sub3=int(input("Enter your marks sub 3:  "))
su1=int(input("Enter your marks out of sub 1:  "))
su2=int(input("Enter your marks out  of sub 2:  "))
su3=int(input("Enter your marks out of sub 3:  "))
t_marks=su1+su2+su3

a=(sub1*100)/su1
b=(sub2*100)/su2
c=(sub3*100)/su3

if(a<33):
    print("fail 1")
elif(b<33):
    print("fail 2")
elif(c<33):
    print("fail 3")
re_pr=(a+b+c)/3
print(re_pr)
if(re_pr>=40):
    print("pass ")
else:
    print("fail ")
