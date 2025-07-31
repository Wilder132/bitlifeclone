import char_base
import random



def career_menu(character):
    """Directs the player to the appropriate job menu based on age."""
    if 14 <= character.c_age < 18:
        part_time_job_menu(character)
    elif character.c_age >= 18:
        full_time_job_menu(character)
    else:
        print("\nYou are too young to get a job. You must be at least 14.")
        input("Press Enter to continue...")
        return

def full_time_job_menu(character):
    """Displays the full-time career menu and handles user choices."""
    while True:
        print("\n--- Career Menu ---")
        print(f"Current Job: {character.c_career}")
        print("1) Look for a job")
        print("2) Quit current job")
        print("3) Back to main menu")

        choice = input("> ")
        if choice == '1':
            find_job(character)
        elif choice == '2':
            if character.c_career != "None":
                print(f"\nYou have quit your job as a {character.c_career}.")
                character.c_career = "None"
                character.c_salary = 0
            else:
                print("\nYou don't have a job to quit.")
            input("Press Enter to continue...")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

def part_time_job_menu(character):
    """Displays the part-time job menu for teenagers."""
    while True:
        print("\n--- Part-Time Jobs ---")
        print(f"Current Part-Time Job: {character.c_part_time_job}")
        print("1) Look for a part-time job")
        print("2) Quit current part-time job")
        print("3) Back to main menu")

        choice = input("> ")
        if choice == '1':
            find_part_time_job(character)
        elif choice == '2':
            if character.c_part_time_job != "None":
                print(f"\nYou have quit your part-time job as a {character.c_part_time_job}.")
                character.c_part_time_job = "None"
                character.c_part_time_salary = 0
            else:
                print("\nYou don't have a part-time job to quit.")
            input("Press Enter to continue...")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

def find_part_time_job(character):
    """Lists available part-time jobs and lets the player apply."""
    if character.c_part_time_job != "None":
        print(f"\nYou already have a part-time job. Quit first to find a new one.")
        input("Press Enter to continue...")
        return

    print("\n--- Available Part-Time Jobs ---")
    available_jobs = char_base.part_time_jobs
    for i, (job_title, min_salary, max_salary) in enumerate(available_jobs):
        print(f"{i + 1}) {job_title} (Annual Salary: ${min_salary:,} - ${max_salary:,})")

    try:
        choice = int(input("\nWhich job would you like to apply for? (0 to cancel)\n> "))
        if choice == 0:
            return

        if 1 <= choice <= len(available_jobs):
            job_title, min_salary, max_salary = available_jobs[choice - 1]
            character.c_part_time_job = job_title
            character.c_part_time_salary = random.randint(min_salary, max_salary)
            print(f"\nYou were hired as a {job_title} with an annual salary of ${character.c_part_time_salary:,}!")
            input("Press Enter to continue...")
    except (ValueError, IndexError):
        print("Invalid input.")

def find_job(character):
    """Lists available jobs and lets the player apply."""
    if character.c_career != "None":
        print(f"\nYou already work as a {character.c_career}. Quit your job first to look for a new one.")
        input("Press Enter to continue...")
        return

    print("\n--- Available Jobs ---")
    available_jobs = char_base.careers

    for i, (job_title, min_salary, max_salary, min_intellect, edu_req) in enumerate(available_jobs):
        req_str = f"IQ: {min_intellect}"
        if edu_req != "None":
            req_str += f", Edu: {edu_req}"
        print(f"{i + 1}) {job_title} (Salary: ${min_salary:,} - ${max_salary:,}) (Requires: {req_str})")

    try:
        choice = int(input("\nWhich job would you like to apply for? (0 to cancel)\n> "))
        if choice == 0:
            return

        if 1 <= choice <= len(available_jobs):
            selected_job = available_jobs[choice - 1]
            job_title, min_salary, max_salary, min_intellect, edu_req = selected_job

            if character.c_intellect < min_intellect:
                print(f"\nUnfortunately, you were not smart enough for the {job_title} position.")
            elif edu_req != "None" and character.education_level != edu_req:
                print(f"\nUnfortunately, you do not have the required education ({edu_req}) for this position.")
            else:
                character.c_salary = random.randint(min_salary, max_salary)
                character.c_career = job_title
                print(f"\nCongratulations! You were hired as a {job_title} with an annual salary of ${character.c_salary:,}.")
            input("Press Enter to continue...")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid job number.")