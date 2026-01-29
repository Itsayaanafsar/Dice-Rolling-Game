import random
count = 0
while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "y":
        rolls = int(input("How many times do you want to roll the dice? "))
        for i in range(rolls):
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print(f"({dice1}, {dice2})")
        count += rolls
        print(f"Total rolls: {count}")
        
    elif choice == "n":
        print("Game ended")
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

