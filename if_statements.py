name = input("Enter name : ").lower()
# if (name == "john"):
#     print(f"{name} is Match")
# elif(name == "jack"):
#     print(f"{name} is a match")
# elif(name == "jane"):
#     print(f"{name} is a match")
# elif(name == "jude"):
#     print(f"{name} is a match")
# else:
#     print("no match")

# Grade analyser

score = int(input("Enter score : "))

if (score >= 90 and score < 101):
    print(f"{name} your grade is A👌")
elif(score < 90 and score >= 70):
    print(f"{name} your Grade is B")
elif(score < 70 and score >= 50):
    print(f"{name} your Grade is C")
elif(score < 50 and score >= 30):
    print(f"{name} your Grade is D")
elif(score < 30 and score >= 10):
    print(f"{name} your Grade is E")
elif(score < 10 and score >= 0):
    print(f"{name} you failed")
else:
    print("Enter valid score")