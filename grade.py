print("Enter your marks: ") 
sum,avg=0,0 
for i in range(6):     
    mark=int(input())     
    sum=sum+mark 
avg=sum/6 
print("Total is : ",sum) 
print("Average is: ",round(avg)) 
if avg > 90:     
    print("A+") 
elif avg > 80:     
    print("A") 
elif avg > 70:     
    print("B+") 
elif avg > 60:     
    print("C") 
else:
    print("Failed")