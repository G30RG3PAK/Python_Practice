import sys

userone = raw_input("What's your name?")
usertwo = raw_input("And...?")
userone_answer = raw_input("%s, choose rock, paper or scissors?" % userone)
usertwo_answer = raw_input("%s, choose rock, paper, or scissors?" % usertwo)


def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock Wins!")
        else:
            return("Paper Wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors Wins!")
        else:
            return("Rock Wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper Wins!")
        else:
            return("Scissors Wins!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors")
        sys.exit()


print(compare(userone_answer, usertwo_answer))


        
