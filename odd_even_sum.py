even_sum,odd_sum=0,0
for i in range(14,36):
    if (i%2==0):
        even_sum=even_sum+i

    else:
        odd_sum=odd_sum+i
print("Even sum is: ",even_sum)
print("Odd sum is: ",odd_sum)