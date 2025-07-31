import char_base
import random

# --- Player Character ---

male_names = char_base.first_names_male
female_names = char_base.first_names_female
last_names = char_base.last_names

def get_gender():
    return random.choice(["Male", "Female"])

def generate_full_name(chosen_gender):
    if chosen_gender == "Male":
        first_name = random.choice(male_names)
    else:
        first_name = random.choice(female_names)

    last_name = random.choice(last_names)

    full_name = f"{first_name} {last_name}"
    return full_name

def generate_health():
    return random.randint(1, 100)

def generate_looks():
    return random.randint(1, 100)

def generate_happy():
    return random.randint(1, 100)

def generate_intellect():
    return random.randint(1, 100)

class player_character:
    def __init__(self):
        self.c_gender = get_gender()
        self.c_fullname = generate_full_name(self.c_gender)
        self.c_age = 0
        self.c_health = generate_health()
        self.c_looks = generate_looks()
        self.c_happy = generate_happy()
        self.c_intellect = generate_intellect()
        self.c_career = "None"
        self.c_salary = 0
        self.c_money = 0
        self.c_expenses = 0
        self.c_living_situation = "Parents' House"
        self.c_stress = 0
        self.marital_status = "Single"
        self.c_part_time_job = "None"
        self.c_part_time_salary = 0
        self.education_level = "None"
        self.school_performance = 50  # 0-100 scale
        self.criminal_record = False
        self.is_in_jail = False
        self.jail_sentence = 0
        self.cause_of_death = "None"
        self.assets = []
        self.diseases = []  # List of current diseases (names)
        self.relationships = []
        generate_parents(self)

    def __str__(self):
        education_info = f"Education: {self.education_level}"
        if "School" in self.education_level or "University" in self.education_level:
            education_info += f" (Performance: {self.school_performance}%)"

        job_info = f"Career: {self.c_career}\nSalary: ${self.c_salary:,}"
        if self.c_part_time_job != "None":
            job_info += f"\nPart-Time Job: {self.c_part_time_job} (${self.c_part_time_salary:,})"

        assets_info = ""
        if self.assets:
            assets_info += "\nAssets:\n"
            for asset in self.assets:
                assets_info += f"  - {asset['name']} (Value: ${int(asset['value']):,}, Condition: {asset['condition']}%)\n"

        status_info = ""
        if self.is_in_jail:
            status_info = f"\nStatus: In Jail ({self.jail_sentence} years remaining)"

        return (f"Name: {self.c_fullname}\n"
                f"Gender: {self.c_gender}\n"
                f"Age: {self.c_age}\n"
                f"Marital Status: {self.marital_status}\n\n"
                f"{education_info}\n"
                f"Living Situation: {self.c_living_situation}\n"
                f"{job_info}\n"
                f"Annual Expenses: ${self.c_expenses:,}\n"
                f"Money: ${self.c_money:,}{assets_info}\n"
                f"{status_info}\n"
                f"--- Stats ---\n"
                f"Health: {self.c_health}%\n"
                f"Looks: {self.c_looks}%\n"
                f"Happiness: {self.c_happy}%\n"
                f"Intellect: {self.c_intellect}%\n"
                f"Stress: {self.c_stress}%")

# --- Non-Player Character (NPC) ---

class NPC:
    """Represents a Non-Player Character in the game."""
    def __init__(self, first_name, last_name, relationship_type, age, player_age):
        self.first_name = first_name
        self.last_name = last_name
        self.relationship_type = relationship_type
        # Set a realistic age relative to the player
        self.age = player_age + random.randint(25, 40) if relationship_type in ["Mother", "Father"] else age
        self.relationship_quality = random.randint(50, 90) # Start with a decent relationship

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.full_name} ({self.relationship_type})"

def generate_parents(player_character):
    """Generates parents for the player character and adds them to the relationships list."""
    player_last_name = player_character.c_fullname.split(" ")[-1]
    
    mother = NPC(random.choice(char_base.first_names_female), player_last_name, "Mother", 0, player_character.c_age)
    father = NPC(random.choice(char_base.first_names_male), player_last_name, "Father", 0, player_character.c_age)
    
    player_character.relationships.extend([mother, father])

def generate_new_npc(player_character):
    """Generates a new random NPC for the player to meet."""
    player_age = player_character.c_age

    if player_age >= 18:
        relationship_type = "Partner"
        age = max(18, player_age + random.randint(-3, 3))
    else:
        relationship_type = "Friend"
        age = max(5, player_age + random.randint(-1, 1))

    gender = random.choice(["Male", "Female"])
    if gender == "Male":
        first_name = random.choice(char_base.first_names_male)
    else:
        first_name = random.choice(char_base.first_names_female)
    
    last_name = random.choice(char_base.last_names)
    return NPC(first_name, last_name, relationship_type, age, player_age)

def generate_child(player_character):
    """Generates a new child for the player."""
    player_last_name = player_character.c_fullname.split(" ")[-1]
    gender = random.choice(["Male", "Female"])
    
    if gender == "Male":
        first_name = random.choice(char_base.first_names_male)
    else:
        first_name = random.choice(char_base.first_names_female)
        
    child = NPC(first_name, player_last_name, "Child", 0, player_character.c_age)
    child.relationship_quality = 100
    player_character.relationships.append(child)
    return child