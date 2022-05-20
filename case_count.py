def upper_case(in_string1):
    upper=0
    #lower=0
    for i in in_string1:
        if i.isupper():
            upper=upper+1
    return(upper)
def lower_case(in_string1):
    #upper=0
    lower=0
    for i in in_string1:
        if i.islower():
            lower=lower+1
    return(lower)
            
in_string=input("String: ")
print("Upper case: ",upper_case(in_string))
print("Lower case: ",lower_case(in_string))