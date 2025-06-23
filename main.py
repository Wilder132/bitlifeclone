import char_gen
import char_base
import graphics

##MainMenu
def main_menu():
    graphics.ascii_mainmenu()
    try:
        keyinput = int(input(">"))
    except ValueError:
        print("ERROR! Choose valid number")
        main_menu()

    ##New Game start
    if keyinput == 1:
        player_character = char_gen.player_character()
        playscreen()
    
    ##Load Character
    if keyinput == 2:
        print("under development")

    ##Past Characters
    if keyinput == 3:
        print("Under Development")

    ##Exit
    if keyinput == 4:
        exit

def playscreen():
    graphics.ascii_playscreen()

main_menu()