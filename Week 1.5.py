c1=int(input())
c2=int(input())
r1=0.10*c1
r2=0.25*c2
total=r1+r2
result="{:.2f}".format(total)
print("Your total refund will be $",result,".",sep="")
