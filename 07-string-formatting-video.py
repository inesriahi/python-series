# String Formatting

# Hi! I am Asma and I am 15 years old.

name = 'Omar'
age = 20

print("Hi! I am Asma and I am 15 years old.")

print("Hi! I am", name, "and I am", age, "years old.")
print("Hi! I am %s and I am %d years old." %(name, age))
print("Hi! I am {} and I am {} years old.".format(name, age))
print(f"Hi! I am {name} and I am {age} years old.")

print()
# The value of 5*3 is 15
print("The value of 5*3 is %d" %(5*3))
print("The value of 5*3 is {}".format(5*3))
print(f"The value of 5*3 is {5*3}")
print()

# An approximation of PI is 22/7
pi = 22/7
print("An approximation of PI is %f" %pi)
print("An approximation of PI is {}".format(pi))
print(f"An approximation of PI is {pi}")
print()


print("An approximation of PI is %.3f" %pi)
print("An approximation of PI is {:.3f}".format(pi))
print(f"An approximation of PI is {pi:.5f}")
print()

# Padding is
print("Hi! I am %10s and I am %10d years old." %(name, age))
print("Hi! I am {:^10s} and I am {:^10d} years old.".format(name, age))
print(f"Hi! I am {name:^10s} and I am {age:010} years old.")
print()

salary = 1.2
print(
    f"{'Name:':<15}{name:>5}",
    f"\n{'Age:':<15}{age:>5}",
    f"\n{'Salary:':<15}{salary:>5}",
)

# Id       |Name     |Age      |Salary
# =========|=========|=========|=========     
# 01       |Omar     |25       |1.2K
# 02       |Ahmed    |31       |2.2K

id1 = '01'
id2 = '02'

name1 = "Omar"
name2 = "Ahmed"

age1 = 25
age2 = 31

salary1 = 1.2
salary2 = 2.2


print(f"{'Id':^9}|{'Name':^9}|{'Age':^9}|{'Salary':^9}")
print(f"{'='*9}|{'='*9}|{'='*9}|{'='*9}")

padding = 20
print(f"{'Id':{padding}}|{'Name':{padding}}|{'Age':{padding}}|{'Salary':{padding}}")
print(f"{'='*padding}|{'='*padding}|{'='*padding}|{'='*padding}")
print(f"{id1:{padding}}|{name1:{padding}}")