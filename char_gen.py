import char_base
import random

male_names = char_base.first_names_male
female_names = char_base.first_name_female
last_names = char_base.last_names

def get_gender():
    return random.choice(["Male", "Female"])

def generate_full_name():
    chosen_gender = get_gender() 
    
    if chosen_gender == "Male":
        first_name = random.choice(male_names)
    else:
        first_name = random.choice(female_names)
        
    last_name = random.choice(last_names)
    
    full_name = f"{first_name} {last_name}"
    return full_name

def generate_health():
    health = random.randint(1, 100)
    return health

def generate_looks():
    looks = random.randint(1, 100)
    return looks

def generate_happy():
    happy = random.randint(1, 100)
    return happy

def generate_intellect():
    intellect = random.randint(1, 100)
    return intellect

class player_character:
    def __init__(self):
        self.c_gender = get_gender()
        self.c_fullname = generate_full_name()
        self.c_age = 0
        self.c_health = generate_health()
        self.c_looks = generate_looks()
        self.c_happy = generate_happy()
        self.c_intellect = generate_intellect()
        self.c_career = "None"
        self.c_stress = 0

    def __str__(self):
        return (f"Name: {self.c_fullname}\n"
                f"Gender: {self.c_gender}\n"
                f"Age: {self.c_age}\n"
                f"Health: {self.c_health}\n"
                f"Looks: {self.c_looks}\n"
                f"Happiness: {self.c_happy}\n"
                f"Intellect: {self.c_intellect}\n"
                f"Career: {self.c_career}\n"
                f"Stress: {self.c_stress}")
    