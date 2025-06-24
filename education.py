import random

UNIVERSITY_TUITION = 20000
UNIVERSITY_ADMISSION_IQ = 60

def education_menu(character):
    """Displays the education menu and handles choices."""
    while True:
        print("\n--- Education ---")
        print(f"Current Level: {character.education_level}")
        if "School" in character.education_level or "University" in character.education_level:
            print(f"School Performance: {character.school_performance}%")

        # Determine available options based on character's state
        is_in_school = "School" in character.education_level and 5 <= character.c_age < 18
        is_in_university = "University" in character.education_level
        can_enroll_university = character.education_level == "High School Diploma"

        if is_in_school:
            print("\n1) Study Harder\n2) Skip Class\n0) Back")
            choice = input("> ")
            if choice == '1': study_harder(character)
            elif choice == '2': skip_class(character)
            elif choice == '0': break
            else: print("Invalid choice.")
        elif is_in_university:
            print("\n1) Study Harder\n0) Back")
            choice = input("> ")
            if choice == '1': study_harder(character)
            elif choice == '0': break
            else: print("Invalid choice.")
        elif can_enroll_university:
            print("\n1) Enroll in University\n0) Back")
            choice = input("> ")
            if choice == '1': enroll_in_university(character)
            elif choice == '0': break
            else: print("Invalid choice.")
        else:
            print("\nThere are no education options available at this time.")
            input("Press Enter to continue...")
            break

def study_harder(character):
    """Improves school performance at the cost of happiness and stress."""
    character.school_performance = min(100, character.school_performance + random.randint(5, 10))
    character.c_happy = max(0, character.c_happy - 5)
    character.c_stress = min(100, character.c_stress + 5)
    print("\nYou hit the books. Your performance improves, but it's tiring.")
    input("Press Enter to continue...")

def skip_class(character):
    """Decreases school performance for a bit of fun."""
    character.school_performance = max(0, character.school_performance - random.randint(5, 10))
    character.c_happy = min(100, character.c_happy + 10)
    print("\nYou skipped class to hang out with friends. It was fun, but your grades might suffer.")
    input("Press Enter to continue...")

def enroll_in_university(character):
    """Handles enrolling in university."""
    print(f"\nUniversity tuition costs ${UNIVERSITY_TUITION:,}.")
    if character.c_intellect < UNIVERSITY_ADMISSION_IQ:
        print(f"Unfortunately, your intellect ({character.c_intellect}) is too low to be accepted. You need at least {UNIVERSITY_ADMISSION_IQ}.")
    elif character.c_money < UNIVERSITY_TUITION:
        print("You don't have enough money for tuition.")
    else:
        character.c_money -= UNIVERSITY_TUITION
        character.education_level = "In University (Year 1)"
        character.school_performance = 50  # Reset performance for university
        character.c_happy = min(100, character.c_happy + 15)
        print("Congratulations! You have been accepted into university and paid the tuition.")
    input("Press Enter to continue...")