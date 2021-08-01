import random
computer_num = random.randint(1, 100)

user_num = input("What is your guess? Choose from 1 to 100.\n")

while not user_num.isnumeric() or int(user_num) > 100 or int(user_num) < 0:
    print("\nEnter only numbers or numbers from 1 to 100.")
    user_num = input("\nWhat is your guess? Choose from 1 to 100.\n")


if (user_num == computer_num):
    print("You're right! Congratulations!")
else:
    result = f"Aw.. Your guess was wrong.\nThe number was {computer_num}."
    print(result)
