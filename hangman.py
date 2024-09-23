def hang():
    import random

    word_list = ["hello", "cat", "bat", "bye"]
    lives = 6

    choice = random.choice(word_list)
    display = ["_"] * len(choice)
    word_length = len(choice)
    end = False

    from hang import stages, logo
    print(logo)

    while not end:
        guess = input("Guess a letter: ").lower()
        for position in range(word_length):
            letter = choice[position]
            if letter == guess:
                display[position] = letter
        if "_" not in display:
            end = True
            print("You guessed the word correctly!")
            print("The word is",choice)
        if guess not in choice:
            lives -= 1
            if lives == 0:
                end = True
                print("You lost!")
                print("The word is", choice)
                break
        print(stages[lives])

    again=input("Do you want to play again? (y/n)").upper()
    if again=="Y":
        hang()
    else:
        end=True
hang()