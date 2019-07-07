from random import choice

def make_laugh_at(person):
    def get_laugh():
        laugh = choice(("HAHAHAA", "LOL"))
        return f"{laugh} {person}"

    return get_laugh

laugh_at = make_laugh_at("Harry")

print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
