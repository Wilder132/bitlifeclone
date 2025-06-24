import entities
import graphics
import aging
import career
import activities
import relationships
import education
import save_load

##MainMenu
def main_menu():
    while True:
        graphics.ascii_mainmenu()
        try:
            keyinput = int(input(">"))

            ##New Game start
            if keyinput == 1:
                player_character = entities.player_character()
                game(player_character)
            
            ##Load Character
            elif keyinput == 2:
                saves = save_load.get_save_slots()
                if not saves:
                    print("\nNo saved games found.")
                    input("Press Enter to continue...")
                    continue
                
                print("\n--- Load Game ---")
                for slot, summary in saves:
                    print(f"{slot}) {summary}")
                print("0) Back")

                try:
                    choice = int(input("> "))
                    if choice == 0:
                        continue
                    
                    loaded_character = save_load.load_character(choice)
                    if loaded_character:
                        game(loaded_character)
                except ValueError:
                    print("Invalid input.")

            ##Past Characters
            elif keyinput == 3:
                print("Under Development")

            ##Exit
            elif keyinput == 4:
                return
            else:
                print("ERROR! Choose a valid number.")

        except ValueError:
            print("ERROR! Choose a valid number.")

def game(character):
    is_alive = True
    while is_alive:
        if character.is_in_jail:
            print(character)
            print("\n--- You are in Jail! ---")
            print(f"You have {character.jail_sentence} years remaining on your sentence.")
            print("You can only age up to serve your time.")
            input("Press Enter to serve another year...")
            is_alive = aging.age_up(character)
            if not is_alive:
                # Handle death in prison
                print(graphics.generate_epitaph(character))
                input("\nPress Enter to return to the main menu...")
            continue # Skip the normal menu

        print(character)
        graphics.ascii_game()
        try:
            keyinput = int(input(">"))

            if keyinput == 1:
                is_alive = aging.age_up(character)
                if not is_alive:
                    print("\n--- You have died ---")
                    print(f"{character.c_fullname} has {character.cause_of_death}.")
                    print(graphics.generate_epitaph(character))
                    input("\nPress Enter to return to the main menu...")
                    # The loop will terminate naturally on the next check
            elif keyinput == 2:
                education.education_menu(character)
            elif keyinput == 3:
                relationships.relationships_menu(character)
            elif keyinput == 4:
                career.career_menu(character)
            elif keyinput == 5:
                activities.activities_menu(character)
            elif keyinput == 6:
                print("\n--- Save Game ---")
                print("Choose a slot to save to (1-5):")
                try:
                    slot = int(input("> "))
                    if 1 <= slot <= 5:
                        if save_load.save_character(character, slot):
                            is_alive = False # Exit game loop to return to main menu
                    else:
                        print("Invalid slot. Please choose 1-5.")
                except ValueError:
                    print("Invalid input.")
            else:
                print("Option not yet implemented.")

        except ValueError:
            print("ERROR! Choose a valid number.")

main_menu()