users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

#extract inactive users:
inactive_users = list(filter(lambda user: not user['tweets'], users)) 
# or,  [user for user in users if not user["tweets"]]
print("\nInactive Users: ", inactive_users)

# extract usernames of inactive users:
usernames = list(map(lambda user: user["username"].upper(), filter(lambda u: not u['tweets'], users)))
# or,  [user["username"].upper() for user in users if not user["tweets"]]
print("\nUsernames: ", usernames)
