import char_base
import random

def activities_menu(character):
    """Displays the main activities menu."""
    while True:
        print("\n--- Activities Menu ---")
        print("1) Mind & Body")
        print("2) Real Estate")
        print("3) Go on Vacation")
        print("4) Assets")
        print("5) Crime")
        print("6) Health")
        print("7) Back to main menu")

        choice = input("> ")
        if choice == '1':
            mind_and_body_menu(character)
        elif choice == '2':
            real_estate_menu(character)
        elif choice == '3':
            vacation_menu(character)
        elif choice == '4':
            assets_menu(character)
        elif choice == '5':            
            crime_menu(character)
        elif choice == '6':
            health_menu(character)
        elif choice == '7':
            break
        else:
            print("Invalid choice.")

def real_estate_menu(character):
    """Handles buying a new house."""
    print("\n--- Real Estate ---")
    print(f"Current Home: {character.c_living_situation}")
    print(f"Your Money: ${character.c_money:,}")
    
    available_properties = char_base.properties
    for i, (name, price, happiness_boost) in enumerate(available_properties):
        print(f"{i + 1}) Buy {name} - ${price:,}")
    
    print("0) Go Back")

    try:
        choice = int(input("> "))
        if choice == 0:
            return
        
        if 1 <= choice <= len(available_properties):
            selected_property = available_properties[choice - 1]
            prop_name, prop_price, prop_boost = selected_property

            if character.c_money >= prop_price:
                character.c_money -= prop_price
                character.c_living_situation = prop_name
                character.c_happy = min(100, character.c_happy + prop_boost)
                print(f"\nCongratulations! You have purchased the {prop_name}.")
            else:
                print("\nYou don't have enough money to buy this property.")
            input("Press Enter to continue...")

    except (ValueError, IndexError):
        print("Invalid input.")

def vacation_menu(character):
    """Handles going on vacation."""
    print("\n--- Go on Vacation ---")
    print(f"Your Money: ${character.c_money:,}")

    vacations = char_base.vacations
    for i, (name, price, happy_boost, stress_relief) in enumerate(vacations):
        print(f"{i + 1}) {name} - ${price:,}")

    print("0) Go Back")

    try:
        choice = int(input("> "))
        if choice == 0:
            return

        if 1 <= choice <= len(vacations):
            selected_vacation = vacations[choice - 1]
            vac_name, vac_price, vac_happy, vac_stress = selected_vacation

            if character.c_money >= vac_price:
                character.c_money -= vac_price
                character.c_happy = min(100, character.c_happy + vac_happy)
                character.c_stress = max(0, character.c_stress - vac_stress)
                print(f"\nYou enjoyed a wonderful vacation to {vac_name}!")
            else:
                print("\nYou don't have enough money for that vacation.")
            input("Press Enter to continue...")
            
    except (ValueError, IndexError):
        print("Invalid input.")

def assets_menu(character):
    """Displays the assets menu for buying and selling."""
    while True:
        print("\n--- Assets ---")
        print(f"Your Money: ${character.c_money:,}")
        if not character.assets:
            print("You do not own any assets.")
        else:
            print("Your Assets:")
            for asset in character.assets:
                print(f"  - {asset['name']} (Value: ${int(asset['value']):,}, Condition: {asset['condition']}%)")
        
        print("\n1) Buy a Car")
        print("2) Sell a Car")
        print("0) Back")

        choice = input("> ")
        if choice == '1':
            buy_car_menu(character)
        elif choice == '2':
            if any(asset['type'] == 'Car' for asset in character.assets):
                sell_car_menu(character)
            else:
                print("You have no cars to sell.")
                input("Press Enter to continue...")
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

def buy_car_menu(character):
    """Handles buying a new car."""
    print("\n--- Car Dealership ---")
    available_cars = char_base.cars
    for i, (name, price, maintenance, decay) in enumerate(available_cars):
        print(f"{i + 1}) {name} - ${price:,} (Maint: ${maintenance}/yr)")
    
    print("0) Go Back")

    try:
        choice = int(input("> "))
        if choice == 0:
            return
        
        if 1 <= choice <= len(available_cars):
            name, price, maintenance, decay = available_cars[choice - 1]

            if character.c_money >= price:
                character.c_money -= price
                new_car = {
                    'type': 'Car', 'name': name, 'purchase_price': price,
                    'value': float(price), 'condition': 100,
                    'maintenance': maintenance, 'decay_rate': decay
                }
                character.assets.append(new_car)
                print(f"\nCongratulations! You have purchased a {name}.")
            else:
                print("\nYou don't have enough money to buy this car.")
            input("Press Enter to continue...")
    except (ValueError, IndexError):
        print("Invalid input.")

def sell_car_menu(character):
    """Handles selling an owned car."""
    print("\n--- Sell a Car ---")
    owned_cars = [asset for asset in character.assets if asset['type'] == 'Car']
    for i, car in enumerate(owned_cars):
        print(f"{i + 1}) {car['name']} (Value: ${int(car['value']):,}, Condition: {car['condition']}%)")
    
    print("0) Go Back")

    try:
        choice = int(input("> "))
        if choice == 0:
            return
        
        if 1 <= choice <= len(owned_cars):
            sold_car = owned_cars[choice - 1]
            character.assets.remove(sold_car)
            sale_price = int(sold_car['value'])
            character.c_money += sale_price
            print(f"\nYou sold your {sold_car['name']} for ${sale_price:,}.")
            input("Press Enter to continue...")
    except (ValueError, IndexError):
        print("Invalid input.")        

def health_menu(character):
    """Displays the health menu for managing diseases."""
    while True:
        print("\n--- Health ---")
        if character.diseases:
            print("Current Conditions:")
            for disease in character.diseases:
                print(f"  - {disease}")
        else:
            print("You are currently healthy.")
        
        print("\n1) Visit the Doctor")
        print("0) Back")

        choice = input("> ")
        if choice == '1':
            visit_doctor(character)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

def visit_doctor(character):
    """Attempts to treat current diseases."""
    total_cost = sum(cost for disease, _, cost, _ in char_base.diseases if disease in character.diseases)
    if character.c_money >= total_cost:
        character.c_money -= total_cost
        character.diseases = []  # Cure all diseases
        print(f"\nYou visited the doctor and paid ${total_cost:,}. You are now cured of all ailments!")
    else:
        print(f"\nYou can't afford to see the doctor. You need ${total_cost:,}.")
    input("Press Enter to continue...")

# --- Mind & Body Functions ---

def mind_and_body_menu(character):
    """Displays the Mind & Body menu and handles choices."""
    while True:
        print("\n--- Mind & Body ---")
        print("1) Go to the Gym ($20)")
        print("2) Read a Book")
        print("3) Meditate")
        print("4) Go for a Walk")
        print("0) Back")

        choice = input("> ")
        if choice == '1':
            go_to_gym(character)
        elif choice == '2':
            read_a_book(character)
        elif choice == '3':
            meditate(character)
        elif choice == '4':
            go_for_a_walk(character)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

def go_to_gym(character):
    """Improves health and happiness at a small cost."""
    cost = 20
    if character.c_money < cost:
        print("\nYou can't afford to go to the gym.")
    else:
        character.c_money -= cost
        character.c_health = min(100, character.c_health + random.randint(2, 5))
        character.c_happy = min(100, character.c_happy + random.randint(1, 3))
        print("\nYou had a great workout at the gym!")
    input("Press Enter to continue...")

def read_a_book(character):
    """Improves intellect and happiness."""
    character.c_intellect = min(100, character.c_intellect + random.randint(2, 5))
    character.c_happy = min(100, character.c_happy + random.randint(1, 3))
    print("\nYou read a fascinating book and feel a little smarter.")
    input("Press Enter to continue...")

def meditate(character):
    """Reduces stress and improves happiness."""
    character.c_stress = max(0, character.c_stress - random.randint(5, 15))
    character.c_happy = min(100, character.c_happy + random.randint(2, 5))
    print("\nYou spend some time meditating and feel much calmer.")
    input("Press Enter to continue...")

def go_for_a_walk(character):
    """Improves health and happiness."""
    character.c_health = min(100, character.c_health + 1)
    character.c_happy = min(100, character.c_happy + random.randint(2, 4))
    print("\nYou went for a refreshing walk in the park.")
    input("Press Enter to continue...")

# --- Crime Functions ---

def crime_menu(character):
    """Displays the crime menu and handles choices."""
    while True:
        print("\n--- Crime ---")
        print("Choose your misdeed wisely.")
        
        available_crimes = char_base.crimes
        for i, (name, min_p, max_p, success, jail) in enumerate(available_crimes):
            print(f"{i + 1}) {name} (Success: {success}%)")
        
        print("0) Get cold feet (Back)")

        try:
            choice = int(input("> "))
            if choice == 0:
                break
            
            if 1 <= choice <= len(available_crimes):
                attempt_crime(character, available_crimes[choice - 1])
                if character.is_in_jail:
                    break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")

def attempt_crime(character, crime):
    """Handles the logic for attempting a crime and its outcome."""
    name, min_payout, max_payout, success_chance, jail_time = crime
    print(f"\nYou attempt to commit {name.lower()}...")
    input("Press Enter to see what happens...")

    if random.randint(1, 100) <= success_chance:
        payout = random.randint(min_payout, max_payout)
        character.c_money += payout
        print(f"\nSuccess! You got away with ${payout:,}.")
    else:
        print(f"\nBUSTED! The police have arrested you.")
        character.is_in_jail = True
        character.jail_sentence = jail_time
        character.criminal_record = True
        if character.c_career != "None":
            print(f"You were fired from your job as a {character.c_career}.")
            character.c_career = "None"
            character.c_salary = 0
        if character.c_part_time_job != "None":
            print(f"You were fired from your part-time job as a {character.c_part_time_job}.")
            character.c_part_time_job = "None"
            character.c_part_time_salary = 0
        spouse = next((p for p in character.relationships if p.relationship_type == "Spouse"), None)
        if spouse:
            print(f"Your spouse, {spouse.first_name}, has divorced you over the scandal.")
            character.relationships.remove(spouse)
            character.marital_status = "Divorced"
            character.c_happy = max(0, character.c_happy - 50)
    
    input("Press Enter to continue...")