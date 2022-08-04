import random
import math

def play():
    user= input("What is your choice?'r' for rock 's' for scissor and 'p' for paper \n")
    user=user.lower()

    computer=random.choice(['r' ,'p' ,'s'])

    if user==computer:
        return (0, user,computer)

    if is_win(user,computer):
        return (1, user,computer)
    
    return (-1,user,computer)

def is_win(player,opponent):

        if (player == 'r' and opponent == 's') or (player== 's' and opponent == 'p') or (player == 'p' and opponent =='r'):
            return True
        return False


def play_best_of(n):
    player_wins=0
    computer_wins=0
    wins_necessory= math.ceil(n/2)

    while player_wins < wins_necessory and computer_wins < wins_necessory :
        result,user,computer = play()

        if result == 0:
            print ('It is a tie , you and your computer have chosen {}.\n'.format(user))

        elif result == 1:
            player_wins+=1
            print('Congratulations!You won, you choose {} and your computer choose {}.\n'.format(user,computer))

        else :
            computer_wins+=1
            print('Computer won!. Better Luck next time.You have chosen {} and you computer have chosen {}.\n'.format(user,computer))
        

    if player_wins > computer_wins :
        print('You have won the best of {} games, what a champ'.format(n))

    else:
        print ('computer won the best of {} games, Try again later'.format(n) )

if __name__ == '__main__':
    play_best_of(5)
    
    



