import random

games_played = 1

print("Welcome to my game! Here are the rules:")
print("")
print("You are an international student and your goal is to reach the CMUQ campus. In order to do so, you will have to pass from four stages. In each stage you will get to choose between two options, but only one of them is the correct choice...\n")

while True:
    ready = input("\nAre you ready to play? (yes/no): ")
    if ready == "yes":
        first_choice = input("\n1st stage: You arrive at your local airport but there is a long queue for security checking. Do you skip or wait (skip/wait): ")

        if first_choice == "wait":
            print("\nWell done, you proceed to the next stage!")
            second_level = input("Second stage: You realize that you are late and you might miss your flight. Do you walk to the gate or run? (walk/run): ")

            if second_level == "run":
                print("\nWell done.. you go to stage three")
                third_level = input("Third stage: You arrive at the airport in Qatar and you have to choose between two gates to go through. (gate 1/gate 2) : ")
                if third_level == "gate 2":
                    print("\nWell done..you move on")
                    fourth_level = input("Fourth Stage: Finally, you have to choose between the taxi or the metro to get to campus. (taxi/metro) ")

                    if fourth_level == "taxi":
                        print("\nYou have successfully reached the CMUQ campus. You win!")
                        print("You won after "+str(games_played))
                        print("attempts")
                        break

                    elif fourth_level == "metro":
                        print("\nwrong option, but it is not over yet. The driver challenges you to a game of rock/paper/scissors. If you win, he'll drop you off', else you lose")
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
                                    print("\nYou chose rock. The driver chose rock. You tied")

                                if comp_choice == 2:
                                    print("\nYou chose rock. The driver chose paper.You lose")
                                    print("You are now lost in Qatar. You lost")
                                    games_played += 1
                                    break

                                if comp_choice == 3:
                                    print("\nYou chose rock. The driver chose scissors. You win.")
                                    print("Well done. You have reached the campus. You win")
                                    print("You won after "+str(games_played))
                                    print("attempts")
                                    break


                            if user_choice == "paper":
                                if comp_choice == 1:
                                    print("\nYou chose paper. The driver chose rock. You win ")
                                    print("Well done. You have reached the campus. You win")
                                    print("You won after "+str(games_played))
                                    print("attempts")
                                    break

                                if comp_choice == 2:
                                    print("\nYou chose paper. The driver chose paper. You tied")

                                if comp_choice == 3:
                                    print("\nYou chose paper. The driver chose scissors. You lose.")
                                    print("You are now lost in Qatar. You lost")
                                    games_played += 1
                                    break

                            if user_choice == "scissors":
                                if comp_choice == 1:
                                    print("\nYou chose scissors. The driver chose rock. You lose.")
                                    print("You are now lost in Qatar. You lost")
                                    games_played += 1
                                    break

                                if comp_choice == 2:
                                    print("\nYou chose scissors. The driver chose paper. You win")
                                    print("Well done. You have reached the campus. You win")
                                    print("You won after "+str(games_played))
                                    print("attempts")
                                    break

                                if comp_choice == 3:
                                    print("\nYou chose scissors. The driver chose scissors. You tied")


                elif third_level == "gate 1":
                    print("\nThis gate is under maintainance and is letting a limited number of people through. A number between 1 and 5 will be generated, if this number is even, you proceed, else you lose")
                    generate_number = input("Generate number? (yes): ")

                    if generate_number == "yes":
                            answer = random.randint(1,5)
                            print(answer)
                            if answer in [1,3,5]:
                                print("\nOdd number. You are now stuck at this gate and can't get through. You lost.")
                                games_played += 1

                            if answer in [2,4]:
                                print("\nEven number. You move on")
                                fourth_level = input("Fourth Stage: Finally, you have to choose between the taxi or the metro to get to campus. (taxi/metro) ")
                                if fourth_level == "taxi":
                                    print("\nYou have successfully reached the CMUQ campus. You win!")
                                    print("You won after "+str(games_played))
                                    print("attempts")
                                    break

                                elif fourth_level == "metro":
                                    print("\nwrong option, but it is not over yet. The driver challenges you to a game of rock/paper/scissors. If you win, he'll drop you off', else you lose")
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
                                                print("\nYou chose rock. The driver chose rock. You tied")

                                            if comp_choice == 2:
                                                print("\nYou chose rock. The driver chose paper. You lose")
                                                print("You are now lost in Qatar. You lost")
                                                games_played += 1
                                                break

                                            if comp_choice == 3:
                                                print("\nYou chose rock. The driver chose scissors. You win.")
                                                print("Well done. You have reached the campus. You win")
                                                print("You won after "+str(games_played))
                                                print("attempts")
                                                break


                                        if user_choice == "paper":
                                            if comp_choice == 1:
                                                print("\nYou chose paper. The driver chose rock. You win ")
                                                print("Well done. You have reached the campus. You win")
                                                print("You won after "+str(games_played))
                                                print("attempts")
                                                break

                                            if comp_choice == 2:
                                                print("\nYou chose paper. The driver chose paper. You tied")

                                            if comp_choice == 3:
                                                print("\nYou chose paper. The driver chose scissors. You lose")
                                                print("You are now lost in Qatar. You lost")
                                                games_played += 1
                                                break

                                        if user_choice == "scissors":
                                            if comp_choice == 1:
                                                print("\nYou chose scissors. The driver chose rock. You lose")
                                                print("You are now lost in Qatar. You lost")
                                                games_played += 1
                                                break

                                            if comp_choice == 2:
                                                print("\nYou chose scissors. The driver chose paper. You win")
                                                print("Well done. You have reached the campus. You win")
                                                print("You won after "+str(games_played))
                                                print("attempts")
                                                break

                                            if comp_choice == 3:
                                                print("\nYou chose scissors. The driver chose scissors. You tied")


            if second_level == "walk":
                print("\nThats the wrong choice, but its not over yet. If you answer the following question correctly, the flight attendent will let you in, otherwise you lose")
                trivia = input("Which country will host the 2020 FIFA World Cup?: ")
                if trivia == "Qatar":
                    print("\nCorrect! You move on")
                    third_level = input("Third stage: You arrive at the airport in Qatar and you have to choose between two gates to go through. (gate 1/gate 2) : ")
                    if third_level == "gate 2":
                        print("\nYou proceed to the next level!")
                        fourth_level = input("Fourth Stage: Finally, you have to choose between the taxi or the metro to get to campus. (taxi/metro) ")

                        if fourth_level == "taxi":
                            print("\nYou have successfully reached the CMUQ campus. You win!")
                            print("You won after "+str(games_played))
                            print("attempts")
                            break

                        elif fourth_level == "metro":
                            print("\nwrong option, but it is not over yet. The driver challenges you to a game of rock/paper/scissors. If you win, he'll drop you off', else you lose")
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
                                        print("\nYou chose rock. The driver chose rock. You tied")

                                    if comp_choice == 2:
                                        print("\nYou chose rock. The driver chose paper. You lose")
                                        print("You are now lost in Qatar. You lost")
                                        games_played += 1
                                        break

                                    if comp_choice == 3:
                                        print("\nYou chose rock. The driver chose scissors. You win.")
                                        print("Well done. You have reached the campus. You win")
                                        print("You won after "+str(games_played))
                                        print("attempts")
                                        break

                                if user_choice == "paper":
                                    if comp_choice == 1:
                                        print("\nYou chose paper. The driver chose rock. You win ")
                                        print("Well done. You have reached the campus. You win")
                                        print("You won after "+str(games_played))
                                        print("attempts")
                                        break

                                    if comp_choice == 2:
                                        print("\nYou chose paper. The driver chose paper. You tied")

                                    if comp_choice == 3:
                                        print("\nYou chose paper. The driver chose scissors. You lose")
                                        print("You are now lost in Qatar. You lost")
                                        games_played += 1
                                        break

                                if user_choice == "scissors":
                                    if comp_choice == 1:
                                        print("\nYou chose scissors. The driver chose rock. You lose")
                                        print("You are now lost in Qatar. You lost")
                                        games_played += 1
                                        break

                                    if comp_choice == 2:
                                        print("\nYou chose scissors. The driver chose paper. You win")

                                        print("Well done. You have reached the campus. You win")
                                        print("You won after "+str(games_played))
                                        print("attempts")
                                        break

                                    if comp_choice == 3:
                                        print("\nYou chose scissors. The driver chose scissors. You tied")


                    if third_level == "gate 1":
                        print("\nThis gate is under maintainance and is letting a limited number of people through. A number between 1 and 5 will be generated, if this number is even, you proceed, else you lose")
                        generate_number = input("Generate number? (yes): ")

                        if generate_number == "yes":
                            answer = random.randint(1,5)
                            print(answer)
                            if answer in [1,3,5]:
                                print("\nOdd number. You are now stuck at this gate and can't get through. You lost.")
                                games_played += 1

                            if answer in [2,4]:
                                print("\nEven number. You move on")
                                fourth_level = input("Fourth Stage: Finally, you have to choose between the taxi or the metro to get to campus. (taxi/metro) ")

                                if fourth_level == "taxi":
                                    print("\nYou have successfully reached the CMUQ campus. You win!")
                                    print("You won after "+str(games_played))
                                    print("attempts")
                                    break

                                elif fourth_level == "metro":
                                    print("\nWrong option, but it is not over yet. The driver challenges you to a game of rock/paper/scissors. If you win, he'll drop you off', else you lose")
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
                                                print("\nYou chose rock. The driver chose rock. You tied")

                                            if comp_choice == 2:
                                                print("\nYou chose rock. The driver chose paper. You lose")
                                                print("You are now lost in Qatar. You lost")
                                                games_played += 1
                                                break

                                            if comp_choice == 3:
                                                print("\nYou chose rock. The driver chose scissors. You win.")
                                                print("Well done. You have reached the campus. You win")
                                                print("You won after "+str(games_played))
                                                print("attempts")
                                                break

                                        if user_choice == "paper":
                                            if comp_choice == 1:
                                                print("\nYou chose paper. The driver chose rock. You win ")
                                                print("Well done. You have reached the campus. You win")
                                                print("You won after "+str(games_played))
                                                print("attempts")
                                                break

                                            if comp_choice == 2:
                                                print("\nYou chose paper. The driver chose paper. You tied")

                                            if comp_choice == 3:
                                                print("\nYou chose paper. The computer chose scissors. You lose")
                                                print("You are now lost in Qatar. You lost")
                                                games_played += 1
                                                break

                                        if user_choice == "scissors":
                                            if comp_choice == 1:
                                                print("\nYou chose scissors. The driver chose rock. You lose")
                                                print("You are now lost in Qatar. You lost")
                                                games_played += 1
                                                break

                                            if comp_choice == 2:
                                                print("\nYou chose scissors. The driver chose paper. You win")
                                                print("Well done. You have reached the campus. You win")
                                                print("You won after "+str(games_played))
                                                print("attempts")
                                                break

                                            if comp_choice == 3:
                                                print("\nYou chose scissors. The driver chose scissors. You tied")

                else:
                    print("\nWrong answer.. your flight attendent is dissapointed in your lack of knowldegde and will not let you in. You lost")
                    games_played += 1


        if first_choice == "skip":
            print("\nYou are stopped for not follwoing instructions at the airport. You lost")
            games_played += 1


    if ready == "no":
        print("\nOkay, come back when you're ready")




