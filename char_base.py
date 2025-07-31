first_names_male = [
    "Aaron", "Adam", "Adrian", "Alan", "Albert", "Alexander", "Andrew", "Anthony", "Arthur", "Austin",
    "Benjamin", "Blake", "Brandon", "Brian", "Caleb", "Cameron", "Charles", "Christian", "Christopher", "Daniel",
    "David", "Dennis", "Donald", "Douglas", "Dylan", "Edward", "Elijah", "Eric", "Ethan", "Evan",
    "Frank", "Gabriel", "George", "Gregory", "Harold", "Harry", "Henry", "Isaac", "Jack", "Jacob",
    "James", "Jason", "Jeffrey", "Jeremy", "Jesse", "John", "Jonathan", "Jordan", "Joseph", "Joshua",
    "Julian", "Justin", "Keith", "Kenneth", "Kevin", "Kyle", "Larry", "Lawrence", "Lee", "Liam",
    "Logan", "Louis", "Lucas", "Luke", "Mark", "Martin", "Matthew", "Michael", "Nathan", "Nicholas",
    "Noah", "Oliver", "Patrick", "Paul", "Peter", "Philip", "Ralph", "Raymond", "Richard", "Robert",
    "Ronald", "Ryan", "Samuel", "Scott", "Sean", "Stephen", "Steven", "Theodore", "Thomas", "Timothy",
    "Travis", "Tyler", "Victor", "Vincent", "Walter", "William", "Zachary", "Owen", "Leo", "Miles"
]

first_names_female = [
    "Abigail", "Addison", "Alexis", "Alice", "Amanda", "Amber", "Andrea", "Angela", "Anna", "Ashley",
    "Audrey", "Ava", "Barbara", "Betty", "Brenda", "Brittany", "Brooke", "Carol", "Catherine", "Charlotte",
    "Chelsea", "Chloe", "Christina", "Christine", "Cindy", "Claire", "Courtney", "Crystal", "Cynthia", "Danielle",
    "Deborah", "Denise", "Diana", "Diane", "Donna", "Dorothy", "Elizabeth", "Emily", "Emma", "Erin",
    "Evelyn", "Faith", "Florence", "Frances", "Gabriella", "Grace", "Hannah", "Heather", "Helen", "Jacqueline",
    "Jamie", "Jane", "Janet", "Jasmine", "Jean", "Jennifer", "Jessica", "Jillian", "Joanne", "Jordan",
    "Josephine", "Joy", "Julia", "Karen", "Katherine", "Kathryn", "Katie", "Kayla", "Kelly", "Kimberly",
    "Kylie", "Laura", "Lauren", "Leah", "Lillian", "Linda", "Lisa", "Louise", "Lucy", "Madison",
    "Margaret", "Maria", "Mary", "Megan", "Melissa", "Mia", "Michelle", "Nancy", "Natalie", "Nicole",
    "Olivia", "Pamela", "Patricia", "Rachel", "Rebecca", "Renata", "Rose", "Ruth", "Samantha", "Sandra",
    "Sarah", "Sharon", "Shirley", "Sofia", "Sophia", "Stephanie", "Susan", "Taylor", "Tiffany", "Victoria"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
    "Phillips", "Evans", "Turner", "Parker", "Collins", "Edwards", "Stewart", "Morris", "Rogers", "Reed",
    "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Cooper", "Richardson", "Cox", "Howard", "Ward",
    "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly", "Sanders", "Price",
    "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long",
    "Patterson", "Hughes", "Washington", "Butler", "Freeman", "Myers", "Bryant", "Frank", "Alexander", "Russell"
]

careers = (
    # Title, Min Salary, Max Salary, Min Intellect, Education Requirement
    ("Fast Food Worker", 10000, 20000, 10, "None"),
    ("Retail Sales Associate", 12000, 22000, 15, "None"),
    ("Waiter/Waitress", 15000, 25000, 15, "None"),
    ("Delivery Driver", 18000, 28000, 20, "None"),
    ("Mail Carrier", 20000, 30000, 25, "High School Diploma"),
    ("Police Officer", 40000, 60000, 50, "High School Diploma"),
    ("Office Manager", 50000, 70000, 60, "High School Diploma"),
    ("Teacher", 30000, 50000, 60, "University Degree"),
    ("Nurse", 35000, 55000, 65, "University Degree"),
    ("Accountant", 45000, 65000, 70, "University Degree"),
    ("Software Developer", 70000, 120000, 80, "University Degree"),
    ("Doctor", 80000, 150000, 90, "University Degree"),
    ("Lawyer", 90000, 180000, 90, "University Degree"),
    ("Financial Analyst", 100000, 200000, 85, "University Degree"),
    ("CEO", 150000, 500000, 95, "University Degree"),
)

properties = (
    # Name, Price, Happiness Boost
    ("Cozy Condo", 150000, 10),
    ("Suburban House", 250000, 15),
    ("Luxury Penthouse", 750000, 20),
    ("Sprawling Mansion", 2000000, 25),
)

vacations = (
    # Name, Price, Happiness Boost, Stress Relief
    ("Budget Cruise", 2000, 10, 15),
    ("Exotic Island Getaway", 5000, 20, 30),
    ("Ski Trip in the Alps", 8000, 25, 35),
    ("Around-the-World Tour", 25000, 50, 75),
)

part_time_jobs = (
    # Title, Min Annual Salary, Max Annual Salary
    ("Babysitter", 2000, 4000),
    ("Dog Walker", 1500, 3500),
    ("Lawn Mower", 2500, 5000),
    ("Paper Route", 1800, 3000),
    ("Grocery Bagger", 3000, 5500),
)

cars = (
    # Name, Price, Annual Maintenance, Condition Decay Rate (per year)
    ("Old Banger", 5000, 1000, 15),
    ("Used Sedan", 12000, 600, 10),
    ("New Hatchback", 25000, 400, 7),
    ("Luxury SUV", 60000, 1500, 5),
    ("Sports Car", 100000, 3000, 8),
)

crimes = (
    # Name, Min Payout, Max Payout, Success Chance (%), Jail Time (years)
    ("Shoplifting", 20, 100, 80, 1),
    ("Burglary", 1000, 5000, 60, 3),
    ("Grand Theft Auto", 10000, 40000, 40, 5),
    ("Bank Robbery", 50000, 250000, 20, 10),
)

diseases = (
    # Name, Health Impact, Treatment Cost, Chance of Getting per Year (%)
    ("Common Cold", -5, 50, 20),
    ("Flu", -15, 100, 10),
    ("Food Poisoning", -10, 80, 5),
    ("Allergies", -2, 200, 30),
)

random_events = [
    {
        "description": "You found a wallet on the street and returned it. The owner rewarded you!",
        "age_min": 16,
        "age_max": 99,
        "stat_changes": {"c_happy": 10, "c_money": ("random", 50, 200)}
    },
    {
        "description": "You caught a nasty flu.",
        "age_min": 5,
        "age_max": 99,
        "stat_changes": {"c_health": -15, "c_happy": -10}
    },
    {
        "description": "You won a small lottery prize!",
        "age_min": 18,
        "age_max": 99,
        "stat_changes": {"c_happy": 15, "c_money": ("random", 500, 2500)}
    },
    {
        "description": "You adopted a stray puppy. Your happiness soars!",
        "age_min": 10,
        "age_max": 80,
        "stat_changes": {"c_happy": 20, "c_stress": -10} # Could add an annual expense later
    },
    {
        "description": "Your favorite sports team won the championship!",
        "age_min": 8,
        "age_max": 99,
        "stat_changes": {"c_happy": 8}
    },
    {
        "description": "You got into a minor fender bender. It's stressful and costly.",
        "age_min": 16,
        "age_max": 90,
        "stat_changes": {"c_happy": -8, "c_stress": 15, "c_health": -2, "c_money": ("random", -750, -250)}
    },
    {
        "description": "You tried a new hobby and discovered a hidden talent.",
        "age_min": 12,
        "age_max": 70,
        "stat_changes": {"c_intellect": 5, "c_happy": 7}
    }
]