import random
random_num = random.randint(1,10)
user_guess = 1000
print(random_num)
while random_num != user_guess:
    print(user_guess)
    user_guess = input(f"Nice try but not really with that ludicrous guess of {user_guess}. Try again: ")