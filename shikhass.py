# no_1 = int(input("enter the no:"))
# no_2 = int(input("enter the no:"))
# ans = no_1 * no_2
# print("Ths sum of two no is:",ans)
# print("thank you")

no = int(input("Enter your no:"))

if no%2==0:
    print(no,"is divisible by 2")
elif no%3==0:
     print(no,"is divisible by 3")
elif no%7==0:
     print(no,"is divisible by 7")
else:
    print(no,"is not divisible by 2,3&7")

print("Thank You!")


print("END")
