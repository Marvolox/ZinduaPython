# # def greet(name):
# #     print(f"Hello {name}")

# # greet("njuguna")

# def sum(num1, num2):
#     suM = num1 + num2
#     print(f"The sum is {suM}")

# sum(7,4)

numbers = [6,7,3,77,23,89,25,99,4,5,66,76,890,345,232,1,0]

# num = int(input("Enter number : "))
def prime (num):
    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is a prime number")

    else:
        print(num,"is not a prime number")

result = map(prime,numbers)
print(list(result))

print(len(numbers))