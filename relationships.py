import random
import entities

def relationships_menu(character):
    """Displays the main relationships menu."""
    while True:
        print("\n--- Relationships ---")
        if not character.relationships:
            print("You don't have any relationships yet.")
            input("Press Enter to continue...")
            return

        for i, person in enumerate(character.relationships):
            print(f"{i + 1}) {person.full_name} ({person.relationship_type}) - Quality: {person.relationship_quality}%")
        
        print("\n--- Actions ---")
        print("F) Find a Friend/Partner")
        print("0) Back to main menu")

        try:
            choice = input("> ").lower()
            if choice == 'f':
                entities.find_someone_new(character)
                continue # Redisplay menu
            elif choice == '0':
                break
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(character.relationships):
                selected_npc = character.relationships[choice_num - 1]
                interact_with_npc(character, selected_npc)
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")

def find_someone_new(character):
    """Allows the player to try and meet a new person."""
    if character.c_age < 5:
        print("\nYou are too young to make friends on your own.")
        input("Press Enter to continue...")
        return

    print("\nYou spend some time trying to meet someone new...")
    
    # Success chance is based on looks and happiness
    success_chance = (character.c_happy + character.c_looks) / 200.0
    if random.random() < success_chance:
        new_npc = entities.generate_new_npc(character)
        character.relationships.append(new_npc)
        print(f"You met {new_npc.full_name}! You are now {new_npc.relationship_type.lower()}s.")
    else:
        print("You failed to make a new connection this time.")
    input("Press Enter to continue...")

def interact_with_npc(character, npc):
    """Handles interactions with a specific NPC."""
    while True:
        print(f"\n--- Interacting with {npc.full_name} ---")
        print(f"Relationship Quality: {npc.relationship_quality}%")
        print("1) Spend Time")
        print("2) Give a Gift ($50)")
        print("3) Have a Conversation")

        # Contextual options for marriage and divorce
        is_partner = npc.relationship_type == "Partner"
        can_propose = is_partner and character.c_age >= 18 and npc.age >= 18 and character.marital_status in ["Single", "Widowed", "Divorced"]
        if can_propose:
            print("4) Propose Marriage")

        is_spouse = npc.relationship_type == "Spouse"
        if is_spouse:
            print("4) Divorce")
            # Add option to have a child if married and of age
            if character.c_age >= 18 and character.c_age < 50:
                print("5) Try for a baby")

        print("0) Go Back")

        choice = input("> ")

        if choice == '1':
            change = random.randint(3, 8)
            npc.relationship_quality = min(100, npc.relationship_quality + change)
            character.c_happy = min(100, character.c_happy + 2)
            print(f"You spent some quality time with {npc.first_name}. Relationship improved.")
            break
        elif choice == '2':
            if character.c_money >= 50:
                character.c_money -= 50
                change = random.randint(5, 15)
                npc.relationship_quality = min(100, npc.relationship_quality + change)
                print(f"You gave {npc.first_name} a nice gift. They loved it!")
            else:
                print("You don't have enough money for a gift.")
            break
        elif choice == '3':
            change = random.randint(-5, 10)
            print(f"You had a {'great' if change > 0 else 'bit of an awkward'} conversation with {npc.first_name}.")
            npc.relationship_quality = min(100, max(0, npc.relationship_quality + change))
            break
        elif choice == '4' and can_propose:
            propose_marriage(character, npc)
            break
        elif choice == '4' and is_spouse:
            divorce(character, npc)
            break
        elif choice == '5' and is_spouse:
            try_for_baby(character, npc)
            break
        elif choice == '0':
            break
    input("Press Enter to continue...")

def propose_marriage(character, npc):
    """Handles the marriage proposal event."""
    print(f"You get down on one knee and ask {npc.first_name} to marry you...")
    
    # Proposal success depends on relationship quality and a bit of luck
    proposal_chance = npc.relationship_quality / 110.0
    
    if random.random() < proposal_chance:
        print(f"{npc.first_name} said yes! You are now married.")
        character.marital_status = "Married"
        npc.relationship_type = "Spouse"
        # The spouse takes the player's last name
        npc.last_name = character.c_fullname.split(" ")[-1]
        character.c_happy = min(100, character.c_happy + 30)
    else:
        print(f"{npc.first_name} rejected your proposal. It's over between you.")
        character.relationships.remove(npc)
        character.c_happy = max(0, character.c_happy - 25)

def divorce(character, npc):
    """Handles the divorce event."""
    print(f"You tell {npc.first_name} that you want a divorce.")
    # In this simple model, divorce is always successful but costly.
    character.relationships.remove(npc)
    character.marital_status = "Divorced"
    character.c_happy = max(0, character.c_happy - 25)
    lost_money = int(character.c_money * 0.5)
    character.c_money -= lost_money
    print(f"The divorce is finalized. You lost ${lost_money:,} in the settlement.")

def try_for_baby(character, spouse):
    """Handles the event of trying to have a child."""
    print(f"You and {spouse.first_name} try to have a baby...")

    # Success chance could be based on age, health, etc.
    success_chance = 0.50 # 50% chance for simplicity
    if random.random() < success_chance:
        new_child = entities.generate_child(character)
        print(f"\nCongratulations! You've had a baby. Welcome {new_child.full_name} to the family!")
        character.c_happy = min(100, character.c_happy + 40)
    else:
        print("\nYou were unsuccessful this time.")
        character.c_happy = max(0, character.c_happy - 5)