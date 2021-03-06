import random

def check_int(userInput):
    try:
        int(userInput)
    except ValueError:
        print "Please enter an integer only!"
        return False
    else:
        return True

def check_range(userInput): 
    if userInput > 101 or userInput < 0:
        print "Please enter an integer between 1 and 100!!"
    else:
        return True

def main():
    name = str(raw_input("Hello, what is your name? "))
    print name + ", I'm thinking of a number between 1 and 100. Try to guess my number."
    the_number = random.randint(1, 100)
    count = 1
    guess = 0

    print(the_number)

    while guess != the_number:
        guess = raw_input("Your guess? ")
    
        if check_int(guess) == True:
            guess = int(guess)
        else:
            continue

        if check_range(guess) == True:
            if guess < the_number:
                print "Your guess is too low, try again."
                count += 1
            elif guess > the_number:
                print "Your guess is too high, try again."
                count += 1
            else:
                print "Well done, " + name + "! You found my number in " + str(count) + " tries!"
        else:
            continue

main()

