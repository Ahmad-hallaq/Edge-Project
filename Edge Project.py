import random


print("Welcome to my game! Here are the rules:")
print("")
print("The game consists of 4 levels, and in each level you will get to choose between two pathways, but only one of them is the correct option. By choosing the right option on each level you win, otherwise it may get more challenging...\n")

ready = input("Are you ready to play? (yes/no): ")
if ready == "yes":
    first_choice = input("1st level: Do want to go left or right? (left/right): ")

    if first_choice == "left":
        print("Well done, you proceed to the next level!")
        second_level = input("do you want to go forward or backward? (forward/backward: ")

        if second_level == "forward":
            print("Well done.. you go to level three")
            third_level = input("Do you want to go up or down? (up/down): ")
            if third_level == "up":
                print("Well done..you move on")
                fourth_level = input("Do want to go straight or to the side? (straight/side) ")

                if fourth_level == "straight":
                    print("You win the game")

                elif fourth_level == "side":
                    print("wrong option, but it is not over yet. You will play a game of rock/paper/scissors, if you win, you win the game, else you lose")
                    while True:
                        def choose_option():
                            user_choice = input("choose either rock,paper, or scissors: ")
                            return user_choice

                        def computer_option():
                            comp_choice = random.randint(1,3)
                            return comp_choice

                        user_choice = choose_option()
                        comp_choice = computer_option()

                        if user_choice == "rock":
                            if comp_choice == 1:
                                print("You chose rock. The computer chose rock. You tied")

                            if comp_choice == 2:
                                print("You chose rock. The computer chose paper. You lose")
                                break

                            if comp_choice == 3:
                                print("You chose rock. The computer chose scissors. You win.")
                                print("Well done. You won the game")
                                break


                        if user_choice == "paper":
                            if comp_choice == 1:
                                print("You chose paper. The computer chose rock. You win ")
                                print("Well done. You won the game")
                                break

                            if comp_choice == 2:
                                print("You chose paper. The computer chose paper. You tied")

                            if comp_choice == 3:
                                print("You chose paper. The computer chose scissors. You lose")
                                break

                        if user_choice == "scissors":
                            if comp_choice == 1:
                                print("You chose scissors. The computer chose rock. You lose")
                                break

                            if comp_choice == 2:
                                print("You chose scissors. The computer chose paper. You win")
                                print("Well done. You win the game")
                                break

                            if comp_choice == 3:
                                print("You chose scissors. The computer chose scissors. You tied")




            elif third_level == "down":
                print("That is the wrong option, but its not over yet. A number between 1 and 5 will be generated, if this number is even, you proceed, else you lose")
                generate_number = input("Generate number? (yes): ")

                if generate_number == "yes":
                        answer = random.randint(1,5)
                        print(answer)
                        if answer in [1,3,5]:
                            print("you lose")

                        if answer in [2,4]:
                            print("you move on")
                            fourth_level = input("Do want to go straight or to the side? (straight/side) ")
                            if fourth_level == "straight":
                                print("You win the game")

                            elif fourth_level == "side":
                                print("wrong option, but it is not over yet. You will play a game of rock/paper/scissors, if you win, you win the game, else you lose")
                                while True:
                                    def choose_option():
                                        user_choice = input("choose either rock,paper, or scissors: ")
                                        return user_choice

                                    def computer_option():
                                        comp_choice = random.randint(1,3)
                                        return comp_choice

                                    user_choice = choose_option()
                                    comp_choice = computer_option()

                                    if user_choice == "rock":
                                        if comp_choice == 1:
                                            print("You chose rock. The computer chose rock. You tied")

                                        if comp_choice == 2:
                                            print("You chose rock. The computer chose paper. You lose")
                                            break

                                        if comp_choice == 3:
                                            print("You chose rock. The computer chose scissors. You win.")
                                            print("Well done. You won the game")
                                            break


                                    if user_choice == "paper":
                                        if comp_choice == 1:
                                            print("You chose paper. The computer chose rock. You win ")
                                            print("Well done. You won the game")
                                            break

                                        if comp_choice == 2:
                                            print("You chose paper. The computer chose paper. You tied")

                                        if comp_choice == 3:
                                            print("You chose paper. The computer chose scissors. You lose")
                                            break

                                    if user_choice == "scissors":
                                        if comp_choice == 1:
                                            print("You chose scissors. The computer chose rock. You lose")
                                            break

                                        if comp_choice == 2:
                                            print("You chose scissors. The computer chose paper. You win")
                                            print("Well done. You win the game")
                                            break

                                        if comp_choice == 3:
                                            print("You chose scissors. The computer chose scissors. You tied")


        if second_level == "backward":
            print("Thats the wrong choice, but its not over yet. If you answer the following question correctly, you will proceed, otherwise you lose")
            trivia = input("Which country will host the 2020 FIFA World Cup?: ")
            if trivia == "Qatar":
                print("Correct! You move on")
                third_level = input("Do want to go up or down? (up/down): ")
                if third_level == "up":
                    print("You proceed to the next level!")
                    fourth_level = input("Do want to go straight or to the side? (straight/side) ")

                    if fourth_level == "straight":
                        print("You win the game")

                    elif fourth_level == "side":
                        print("wrong option, but it is not over yet. You will play a game of rock/paper/scissors, if you win, you win the game, else you lose")
                        while True:
                            def choose_option():
                                user_choice = input("choose either rock,paper, or scissors: ")
                                return user_choice

                            def computer_option():
                                comp_choice = random.randint(1,3)
                                return comp_choice

                            user_choice = choose_option()
                            comp_choice = computer_option()

                            if user_choice == "rock":
                                if comp_choice == 1:
                                    print("You chose rock. The computer chose rock. You tied")

                                if comp_choice == 2:
                                    print("You chose rock. The computer chose paper. You lose")
                                    break

                                if comp_choice == 3:
                                    print("You chose rock. The computer chose scissors. You win.")
                                    print("Well done. You won the game")
                                    break

                            if user_choice == "paper":
                                if comp_choice == 1:
                                    print("You chose paper. The computer chose rock. You win ")
                                    print("Well done. You won the game")
                                    break

                                if comp_choice == 2:
                                    print("You chose paper. The computer chose paper. You tied")

                                if comp_choice == 3:
                                    print("You chose paper. The computer chose scissors. You lose")
                                    break

                            if user_choice == "scissors":
                                if comp_choice == 1:
                                    print("You chose scissors. The computer chose rock. You lose")
                                    break

                                if comp_choice == 2:
                                    print("You chose scissors. The computer chose paper. You win")
                                    break
                                    print("Well done. You win the game")

                                if comp_choice == 3:
                                    print("You chose scissors. The computer chose scissors. You tied")



                if third_level == "down":
                    print("Thats the wrong option, but you get another chance. A number between 1 and 5 will be generated, if this number is even, you proceed, else you lose")
                    generate_number = input("Generate number? (yes): ")

                    if generate_number == "yes":
                        answer = random.randint(1,5)
                        print(answer)
                        if answer in [1,3,5]:
                            print("you lose")

                        if answer in [2,4]:
                            print("you move on")
                            fourth_level = input("Do want to go straight or to the side? (straight/side) ")

                            if fourth_level == "straight":
                                print("You win the game")

                            elif fourth_level == "side":
                                print("wrong option, but it is not over yet. You will play a game of rock/paper/scissors, if you win, you win the game, else you lose")
                                while True:
                                    def choose_option():
                                        user_choice = input("choose either rock,paper, or scissors: ")
                                        return user_choice

                                    def computer_option():
                                        comp_choice = random.randint(1,3)
                                        return comp_choice

                                    user_choice = choose_option()
                                    comp_choice = computer_option()

                                    if user_choice == "rock":
                                        if comp_choice == 1:
                                            print("You chose rock. The computer chose rock. You tied")

                                        if comp_choice == 2:
                                            print("You chose rock. The computer chose paper. You lose")
                                            break

                                        if comp_choice == 3:
                                            print("You chose rock. The computer chose scissors. You win.")
                                            print("Well done. You won the game")
                                            break

                                    if user_choice == "paper":
                                        if comp_choice == 1:
                                            print("You chose paper. The computer chose rock. You win ")
                                            print("Well done. You won the game")
                                            break

                                        if comp_choice == 2:
                                            print("You chose paper. The computer chose paper. You tied")

                                        if comp_choice == 3:
                                            print("You chose paper. The computer chose scissors. You lose")
                                            break

                                    if user_choice == "scissors":
                                        if comp_choice == 1:
                                            print("You chose scissors. The computer chose rock. You lose")
                                            break

                                        if comp_choice == 2:
                                            print("You chose scissors. The computer chose paper. You win")
                                            print("Well done. You win the game")
                                            break

                                        if comp_choice == 3:
                                            print("You chose scissors. The computer chose scissors. You tied")

            else:
                print("Wrong answer.. you lose")


    if first_choice == "right":
        print("you lost")


if ready == "no":
    print(":( Okay, come back when you're ready")




