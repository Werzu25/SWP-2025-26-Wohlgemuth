
a = 0
try:
    a = int(input("enter a number: "))
except ValueError:
    print("invalid input")
else:
    print("a is", a)
finally:
    print("executing finally clause")

if a > 5:
    print("a greater than 5")
elif a == 5:
    print("a equal to 5")
else:
    print("a less than 5")

for i in range(5,20,3):
    print(i)
x = 0
while x < 20:
    if x == 18:
        break
    if x == 5:
        x += 2
        print("continue jumps to the next iteration of a loop")
        continue
    if x == 10:
        print("pass is a placeholder function")
        pass
    x += 1
    print(x)

list1 = [1,2,3,4,5]
