answer0 = [num for num in [1,2,3,4] if num in [3,4,5,6]]
answer1 = [name[::-1].lower() for name in ["Elie", "Tim", "Matt"]]
names = ["Ellie", "Tim", "Matt"]
answer2 = [name[0] for name in names]
numbers = [1,2,3,4,5,6]
answer3 = [num for num in numbers if num % 2 == 0]
answer4 =  [num for num in range(1, 101) if num % 12 == 0]
answer5 = [letter for letter in 'amazing' if letter not in 'aeiou']
answer6 = [[num for num in range(3)] for high_num in range(3)]
answer7 = [[num for num in range(10)] for high_num in range(10)]