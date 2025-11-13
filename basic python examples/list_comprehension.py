from itertools import count

data = [
    ("Anna", 1),
    ("Bernd", 3),
    ("Clara", 2),
    ("David", 5),
    ("Eva", 4),
    ("Felix", 1),
    ("Gina", 2),
    ("Hannah", 5),
    ("Ivan", 3),
    ("Julia", 1)
]

checked_list = [result for result in data if (result[1] < 3 and (result[0][0].lower() in "aeiou"))]
print(checked_list)

grades_min_two = {result for _,result in data if [n for _, n in data].count(result) >= 2}
print(grades_min_two)

students = {name:6-grade for name,grade in data if grade != 5}
print(students)