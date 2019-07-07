midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ["dan", "ang", "kate"]

final_grades = { pair[0]: max(pair[1], pair[2]) for pair in zip(students, midterms, finals) }
# or, dict(zip(students, map(lambda pair: max(pair), zip(midterms, finals))))

print(final_grades)
