def Nim():
    import random
    place = input("Would you like to go first(y/n)? ")
    obj_num = 21
    count = 1
    if place == "y":
        while obj_num > 0:
            print(obj_num, "objects remain")
            take_num = int(input("Choose 1, 2, or 3: "))
            if take_num == 1 or take_num == 2 or take_num == 3:
                obj_num = obj_num - take_num
                take_num = random.randint(1,3)
                print(obj_num, "objects remain, I'll take", take_num)
                obj_num = obj_num - take_num
                count += 1
            else:
                print("Error")
        if count // 2 == 0:
            print("I win!")
        else:
            print("You win!")
    elif place == "n":
            while obj_num > 0:
                take_num = random.randint(1,3)
                print(obj_num, "objects remain, I'll take", take_num)
                obj_num = obj_num - take_num
                print(obj_num, "objects remain")
                take_num = int(input("Choose 1, 2, or 3: "))
                if take_num == 1 or take_num == 2 or take_num == 3:
                    obj_num = obj_num - take_num
                    count += 1
                else:
                    print("Error")
            if count // 2 == 0:
                print("You win!")
            else:
                print("I win!")
    else:
        print("Error")

