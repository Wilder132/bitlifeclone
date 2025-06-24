def ascii_game():
    print("""
    #################
        1)Age +1
        2)Education
        3)Relationships
        4)Career
        5)Activities
        6)Save and Quit
          """)

def ascii_mainmenu():
    print("""
    ___ _              _    _  __     
    | _ | |___ ___ _ __| |  (_)/ _|___ 
    | _ | / -_/ -_| '_ | |__| |  _/ -_)
    |___|_\___\___| .__|____|_|_| \___|
                |_|                  

    BleepLife, text-based life simulator:
        1)Create New Character
        2)Load Character
        3)My past characters
        4)Exit
    """)

def generate_epitaph(character):
    """Generates a personalized epitaph based on the character's life."""

    name = character.c_fullname
    age = character.c_age
    money = character.c_money
    career = character.c_career

    if age < 18:
        lifespan_desc = "a tragically short"
    elif age < 40:
        lifespan_desc = "a short"
    elif age < 70:
        lifespan_desc = "a full"
    else:
        lifespan_desc = "a long and storied"

    if career == "None":
        career_desc = "never settled into a career."
    elif character.c_salary > 100000:
        career_desc = f"had a legendary career as a {career}."
    elif character.c_salary > 50000:
        career_desc = f"had a successful career as a {career}."
    else:
        career_desc = f"worked diligently as a {career}."

    if money < 0:
        wealth_desc = f"a mountain of debt amounting to ${abs(money):,}."
    elif money < 10000:
        wealth_desc = "very little to their name."
    elif money < 100000:
        wealth_desc = f"a modest sum of ${money:,}."
    elif money < 1000000:
        wealth_desc = f"a respectable fortune of ${money:,}."
    else:
        wealth_desc = f"an enormous fortune of ${money:,}."

    spouse = next((p for p in character.relationships if p.relationship_type == "Spouse"), None)
    children = [p for p in character.relationships if "Child" in p.relationship_type]

    family_desc = "They left no immediate family."
    if spouse and children:
        family_desc = f"They are survived by their loving spouse, {spouse.first_name}, and {len(children)} children."
    elif spouse:
        family_desc = f"They are survived by their loving spouse, {spouse.first_name}."
    elif children:
        family_desc = f"They are survived by {len(children)} children."

    return (
        f"\nHere lies {name}.\n"
        f"They lived {lifespan_desc} life of {age} years.\n"
        f"Professionally, they {career_desc}\n"
        f"Financially, they left behind {wealth_desc}\n"
        f"{family_desc}"
    )