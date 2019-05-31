""" Python Functions """

def user_data(**kwargs):
    print(f"\n{kwargs}")
    for key, value in kwargs.items():
        yield f"{key}: {value}"

for data in user_data(name = "Harry", age = 26,  color = "Teal"):
    print(data)
for data in user_data(name = "Larry", age = 46,  color = "Blue"):
    print(data)
