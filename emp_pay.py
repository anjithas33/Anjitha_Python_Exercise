eid=int(input("Enter empid: ")) 
ename=input("Enter employee name: ") 
basic=int(input("Enter the basic pay: "))  
hra,net=0,0 
da=0  
if basic > 10000 :     
    hra=basic * .15     
    da=basic * 0.08     
    net=basic + hra + da     
    print("HRA :",hra)     
    print("DA : ",da)     
    print("Net pay: Rs.",net)  
elif basic > 5000 and basic < 10000 :     
    hra=basic * .10     
    da=basic * 0.05     
    net=basic + hra + da     
    print("HRA :",hra)     
    print("DA : ",da)     
    print("Net pay: Rs.",net)   
elif basic < 5000 :     
    hra=basic * .15     
    da=basic * 0.08    
    net=basic + hra + da     
    print("HRA :",hra)     
    print("DA : ",da)     
    print("Net pay: Rs.",net)    
