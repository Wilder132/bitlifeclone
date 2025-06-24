import random
import char_base

# A constant for the chance of a random event happening each year (e.g., 0.25 = 25%)
EVENT_CHANCE = 0.25

# The age at which natural death becomes a possibility
OLD_AGE_START = 80

# --- Expense Constants ---
HOUSING_COSTS = {
    "Parents' House": 0,
    "Rented Apartment": 12000,
    "Cozy Condo": 15000,
    "Suburban House": 25000,
    "Luxury Penthouse": 75000,
    "Sprawling Mansion": 150000,
}
TAX_RATE = 0.20
CHILD_COST_PER_YEAR = 8000

def update_annual_expenses(character):
    """Calculates and updates the character's total annual expenses."""
    if character.c_age == 18 and character.c_living_situation == "Parents' House":
        character.c_living_situation = "Rented Apartment"
        print("\n--- Life Change ---")
        print("You've turned 18 and moved out of your parents' house into a rented apartment.")
        input("Press Enter to continue...")

    housing_cost = HOUSING_COSTS.get(character.c_living_situation, 0)
    total_income = character.c_salary + character.c_part_time_salary
    tax_cost = int(total_income * TAX_RATE)
    child_count = sum(1 for person in character.relationships if person.relationship_type == "Child")
    child_rearing_cost = child_count * CHILD_COST_PER_YEAR
    maintenance_cost = sum(asset['maintenance'] for asset in character.assets)
    character.c_expenses = housing_cost + tax_cost + child_rearing_cost + maintenance_cost

def age_up(character):
    """
    Ages the character up by one year.
    Handles finances, stat changes, random events, and death checks.
    Returns True if the character survives the year, False otherwise.
    """
    character.c_age += 1

    # --- Jail Logic ---
    if character.is_in_jail:
        print("\nYou spend a lonely year behind bars.")
        character.jail_sentence -= 1
        character.c_happy = max(0, character.c_happy - 10) # Jail is depressing
        if character.jail_sentence <= 0:
            character.is_in_jail = False
            print("You have been released from prison!")
        input("Press Enter to continue...")
        return True # Skip the rest of the aging logic for this year

    # --- Education Progression ---
    if character.c_age == 5:
        character.education_level = "Elementary School"
        print("\n--- Life Change ---\nYou have started Elementary School.")
        input("Press Enter to continue...")
    elif character.c_age == 14:
        character.education_level = "High School"
        print("\n--- Life Change ---\nYou have started High School.")
        input("Press Enter to continue...")
    
    if character.c_age == 18 and character.education_level == "High School":
        character.education_level = "High School Diploma"
        character.c_happy = min(100, character.c_happy + 20)
        print("\n--- Life Change ---\nYou have graduated from High School!")

        if character.c_part_time_job != "None":
            print(f"You've also left your part-time job as a {character.c_part_time_job} to focus on your future.")
            character.c_part_time_job = "None"
            character.c_part_time_salary = 0

        input("Press Enter to continue...")
    
    if "In University" in character.education_level:
        year = int(character.education_level.split(" ")[-1][:-1])
        if year < 4:
            character.education_level = f"In University (Year {year + 1})"
        else:
            character.education_level = "University Degree"
            character.c_intellect = min(100, character.c_intellect + random.randint(10, 20))
            character.c_happy = min(100, character.c_happy + 25)
            print("\n--- Life Change ---\nYou have graduated from University with a degree!")
            input("Press Enter to continue...")

    if "School" in character.education_level or "University" in character.education_level:
        # Performance naturally drifts towards 50
        character.school_performance = (character.school_performance + 50) // 2
        # Intellect changes based on performance (e.g., perf 70 -> +2 IQ, perf 30 -> -2 IQ)
        intellect_change = (character.school_performance - 50) // 10
        character.c_intellect = min(100, max(0, character.c_intellect + intellect_change))

    # --- Asset Depreciation ---
    for asset in character.assets:
        # Condition decreases by a set rate, plus a small random factor
        asset['condition'] = max(0, asset['condition'] - (asset['decay_rate'] + random.randint(0, 2)))
        # Value is based on the original price and current condition
        asset['value'] = asset['purchase_price'] * (asset['condition'] / 100.0)

    # --- Marriage bonus ---
    if character.marital_status == "Married":
        # A small, consistent happiness boost from a stable marriage
        character.c_happy = min(100, character.c_happy + 1)

    # --- Relationship Aging ---
    # Use a copy of the list to allow for modification during iteration (e.g., removing a deceased NPC)
    for person in character.relationships[:]:
        person.age += 1
        # Natural decay of relationship quality if not maintained
        person.relationship_quality = max(0, person.relationship_quality - random.randint(0, 2))

        # Check if a child becomes an adult and moves out
        if person.relationship_type == "Child" and person.age == 18:
            print(f"\n--- Life Change ---\nYour child, {person.full_name}, has turned 18 and moved out of the house.")
            person.relationship_type = "Adult Child"
            input("Press Enter to continue...")
        
        # Check for NPC death from old age
        if person.age > OLD_AGE_START:
            npc_death_chance = (person.age - OLD_AGE_START) / 40.0
            if random.random() < npc_death_chance:
                print(f"\n--- Sad News ---\nYour {person.relationship_type}, {person.full_name}, has passed away at the age of {person.age}.")
                if person.relationship_type == "Spouse":
                    character.marital_status = "Widowed"
                character.relationships.remove(person)
                character.c_happy = max(0, character.c_happy - 20) # Grieving

    # --- Death Checks ---
    # Check for death from old age (probabilistic)
    if character.c_age > OLD_AGE_START:
        # The chance of dying increases each year after OLD_AGE_START.
        # At age 100, this is a 50% chance. At age 120, it's 100%.
        death_chance = (character.c_age - OLD_AGE_START) / 40.0
        if random.random() < death_chance:
            character.cause_of_death = f"died peacefully of old age at {character.c_age}"
            return False

    # --- Update and apply expenses ---
    update_annual_expenses(character)

    # --- Handle finances ---
    total_income = character.c_salary + character.c_part_time_salary
    net_income = total_income - character.c_expenses
    character.c_money += net_income

    # --- Standard stat fluctuation ---
    character.c_health = random.randint(max(1, character.c_health - 5), min(100, character.c_health + 5))
    character.c_looks = random.randint(max(1, character.c_looks - 5), min(100, character.c_looks + 5))
    character.c_happy = random.randint(max(1, character.c_happy - 5), min(100, character.c_happy + 5))
    character.c_intellect = random.randint(max(1, character.c_intellect - 5), min(100, character.c_intellect + 5))

    # Check for death from poor health (after stat changes)
    if character.c_health <= 0:
        character.cause_of_death = f"died at the age of {character.c_age} from poor health"
        return False

    # --- Random Event Logic ---
    if random.random() < EVENT_CHANCE:
        # Find all events that are valid for the character's current age
        possible_events = [
            event for event in char_base.random_events
            if event["age_min"] <= character.c_age <= event["age_max"]
        ]

        if possible_events:
            # Pick one event from the list of possible events
            chosen_event = random.choice(possible_events)

            print("\n--- Something happened this year! ---")
            print(chosen_event["description"])

            # Apply the stat changes from the event, ensuring they stay within bounds
            for stat, change_info in chosen_event["stat_changes"].items():
                change_value = 0
                if isinstance(change_info, tuple) and change_info[0] == "random":
                    # It's a random range: ("random", min, max)
                    change_value = random.randint(change_info[1], change_info[2])
                else:
                    # It's a fixed value
                    change_value = change_info

                current_value = getattr(character, stat, 0)
                new_value = current_value + change_value

                # Money is not clamped, other stats are
                setattr(character, stat, new_value if stat == "c_money" else max(0, min(100, new_value)))
            
            input("Press Enter to continue...")
    
    return True # Survived the year