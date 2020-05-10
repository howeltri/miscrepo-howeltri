new_dict = {num: num**2 for num in [1,2,3,4,5]}
instructor = {'name': "sam", 'city': 'ashburn', 'pal': 'scout'}
yelling_instructor = {key.upper():val.upper() for key, val in instructor.items()}
yelling_instructor_logic = {(key.upper() if key == "pal" else key):val.upper() for key, val in instructor.items()}
answer = {list1[i]:list2[i] for i in range(0, len(list1))}
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
#The three of these would work
answer = {persons[0]:persons[1] for persons in person}
answer = {k:v for k,v in person}
answer = dict(person)
answer = {letter:0 for letter in 'aeiou'}
answer = {asc:chr(asc) for asc in range(65,91)}
return {letter: value.count(letter) for letter in value}