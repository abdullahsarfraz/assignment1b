"""
FINAL ASSIGNMENT - BLACK JACK
"""
import random
print('WELCOME TO BLACK JACK.')

def main():
    """
    New Game
    """

    while True:
        start = input('Do you wish to start a new game? (y/n): ')
        if start[:1] == 'y':
            print('Lets play')
            input('Press Enter to continue.')
            break
        elif start[:1] == 'n':
            print('See you later.')
            exit()
        else:
            pass

    pcard1 = random.randint(1, 10)
    pcard2 = random.randint(1, 10)
    ptotal = pcard1 + pcard2
    dcard1 = random.randint(1, 10)
    dcard2 = random.randint(1, 10)
    dtotal = dcard1 + dcard2
    print(f'You draw a {pcard1} and a {pcard2}. Your total is {ptotal}.')
    print(f'Dealer draws a {dcard1} and a hidden card.')



    while True:
        hitstand = input('Hit or Stand? (h/s): ')
        if hitstand[:1] == 'h':
            newpcard = random.randint(1, 10)
            ptotal += newpcard
            if ptotal > 21:
                print(f'You draw a {newpcard}. You total is {ptotal}.')
                print('*****DEALER WON*****')
                main()
            elif ptotal == 21:
                print(f'You draw a {newpcard}. You total is 21. Dealers turn.')
                input('Press Enter to continue.')
                break
            else:
                print(f'you draw a {newpcard}. Your total is {ptotal}.')
        elif hitstand[:1] == 's':
            print('Dealers turn')
            input('Press Enter to continue.')
            break
        else:
            pass


    print(f'Dealer draws his hidden card and it is {dcard2}. Dealers total is {dtotal}.')

    while True:
        if dtotal >= ptotal and dtotal < 22:
            print('*****DEALER WON*****')
            main()
        elif dtotal <= 16:
            input('Press Enter to continue.')
            newdcard = random.randint(1, 10)
            dtotal += newdcard
            print(f'Dealer draws a {newdcard}. Dealers total is {dtotal}.')
        elif dtotal > 21:
            print('*****YOU WON******')
            main()
        else:
            break

    if dtotal >= ptotal:
        print('*****DEALER WON*****')
        main()
    else:
        print('*****YOU WON*****')
        main()


main()
