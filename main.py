import random
p = 0
co = 0
while True:
    print("Rock Paper Scissors!")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    if p == 3:
        print("Player: Humans Better than robots!")
        break
    elif co == 3:
        print("Computer: Robots will take over humanity MUAAHAHA!")
        break
    a = int(input("Please make a choice"))
    c = random.randint(1, 3)
    if a == 1 and c == 1:
        print(" ")
        print("Draw!")
        print(" ")
    elif a == 2 and c == 2:
        print(" ")
        print("Draw!")
        print(" ")
    elif a == 3 and c == 3:
        print(" ")
        print("Draw!")
        print(" ")
    elif a == 1 and c == 2:
        print(" ")
        print(f"You lose! Computer chose {c}!")
        print(" ")
        co += 1
        print(" ")
    elif a == 1 and c == 3:
        print(" ")
        print(f"You win! Computer chose {c}!")
        print(" ")
        p += 1
        print(" ")
    elif a == 2 and c == 1:
        print(" ")
        print(f"You Win! Computer chose {c}!")
        print(" ")
        p += 1
        print(" ")
    elif a == 2 and c == 3:
        print(" ")
        print(f"You lose! Computer chose {c}!")
        print(" ")
        co += 1
        print(" ")
    elif a == 3 and c == 1:
        print(" ")
        print(f"You lose! Computer chose {c}!")
        print(" ")
        co += 1
        print(" ")
    elif a == 3 and c == 2:
        print(" ")
        print(f"You win! Computer chose {c}!")
        print(" ")
        p += 1
        print(" ")
    else:
        print(" ")
        print("ERROR!")
        print(" ")
