""" Python Lambdas """

players =  [ # For, 5th June 2019
    "Shikhar Dhawan", # Open
    "Rohit Sharma", # Open
    "Virat Kohli", # 3
    "KL Rahul", # 4
    "Vijay Shankar", # 5
    "MS Dhoni", # 6
    "Ravindra Jadeja", # 7
    "Hardik Pandya", # 8
    "Kuldeep Yadav", # 9
    "Mohammed Shami", # 10
    "Jasprit Bumrah", # 11
]

""" Maps """
team = list(map(lambda player: player.upper(), players))
# or, [player.upper() for player in players]
print("\nAll Team Members with uppercase: ", team)

""" Filter """
# or, [player for player in players if player[0].lower() == "v"]
players_with_v = list(filter(lambda player: player[0].lower() == "v" , players))
print("\nAll Team Members with v as first_letter: ", players_with_v)

