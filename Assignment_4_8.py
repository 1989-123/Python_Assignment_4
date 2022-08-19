# Write a python script to calculate simple interest

p = float(input("Enter principle amount: "))
r = float(input("Enter rate of intrest: "))
t = int(input("Enter time: "))
si = (p * r *t) / 100
print("Simple intrest is:",si)
