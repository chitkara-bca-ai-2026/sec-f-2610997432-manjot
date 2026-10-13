a = int(input())
if a<=100:
    bill=a*0
elif a<=200:
    bill=(a-100)*5
elif a<=300:
    bill=((a-200)*10)+500
else:
    bill= ((a-200)*10)+650
print ("Total Bill = ",bill)

