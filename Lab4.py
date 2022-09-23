
#import modules needed
import random

#defining play again function with while loop.Asking User.Yes/Y to play again , No/N to end game.
def play_again():
    user_input = input('Would you like to play again? Enter Yes/Y or No/N: ==>') 
    while user_input != 'Yes' and user_input != 'Y' and user_input != 'No' and user_input != 'N':
        user_input = input('Error. Enter Yes/Y or No/N. Try again.\nWould you like to play again?: ===>')
    if user_input == 'Yes' or user_input == 'Y':
        return True
    else:
        print('Thanks for playing!')
        return False
        

#defining wager function. Asking User their wager. If not between 0 and their bank, ask again
def get_wager(bank):
    wager = int(input('How much would chips would you like to wager?: '))
    while wager <= 0 or wager > bank:
        if wager <= 0:
            wager = int(input('Please enter a wage above 0: '))
        else:
            wager = int(input('You cannot gamble more than you have. Please enter a wage less than or equal to the chips you have: '))
    return wager


    
    
# defining a function for slot machine. Getting 3 reel results.
def get_slot_results():
    reel1 = random.randint(1,10)
    reel2 = random.randint(1,10)
    reel3 = random.randint(1,10)

    return reel1, reel2, reel3

#defining function for the matches of the slot function. return how many reels match
def get_matches(reela, reelb, reelc):
    if reela == reelb:
        if reela == reelc:
            return 3
        else:
            return 2
    else:
        if reela == reelc:
            return 2
        else:
            return 0
    

#defining function to ask how many chips user wants to play with, needs to be between 0 and 100, inclusive.
def get_bank():
    x = int(input('How many chips do you want to play with?: '))
    while x <= 0 or x >= 101:
        x = int(input('Please enter number between 0 through 100: '))

    return x


# defining feunction that returns the amount won depending on user wager and results of the slot machine
def get_payout(wager, matches):
    if matches == 3:
        payout = wager * 10
    if matches == 2:
        payout = wager * 3
    if matches == 0:
        payout = wager * -1

    return payout


#main program
if __name__ == "__main__":

    #welcoming user to game
    print('Welcome to Slots! Gamble wisely')
    print()

    #play again loop
    playing = True
    while playing == True:

        #setting up variables
        print()
        banki = get_bank()
        bank = banki
        most = banki
        spin = 0

        #runs game while play gain is True
        while True:  

        #running the game
            wager = get_wager(bank)
            print()

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()


            #counting spins
            spin +=1

            #saving most chips during game
            if bank > most:
                most = bank

            #breaking loop if user is broke
            if bank == 0:
                break
            
        
            
        #Telling user game is over,    
        print("You lost all", banki, "chips in", spin, "spins")
        print("The most chips you had was",most )
        print()

        #asking user if they would like to play again
        playing = play_again()
        
    
