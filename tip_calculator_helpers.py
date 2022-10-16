def cost_of_food_user_input():
    cost_of_food = input('Please enter cost of food ')
    try:
        cost_of_food = int(float(cost_of_food))
        if cost_of_food <= 0:
            print('Please enter a number larger than 0')
            return cost_of_food_user_input()
        else:
            return cost_of_food
    except ValueError:
        print("You didn't enter valid cost for the food, please try again")
        return cost_of_food_user_input()

def number_of_people_user_input():
    number_of_people = input('Please enter number of people splitting the bill ')
    try:
        number_of_people = int(number_of_people)
        if number_of_people <= 0:
            print('Number of people needs to be larger than 0')
            return number_of_people_user_input()
        else:
            return number_of_people
    except ValueError:
        print("You didn't enter valid number of people splitting the bill, please try again")
        return number_of_people_user_input()

def tip_user_input(cost_of_food):
    tip = input(f'What percentage of ${cost_of_food} you like to give in the form of a tip? ')
    try:
        tip = int(tip)
        if tip < 0:
            print('Tip needs to be zero or higher')
            return tip_user_input()
        else:
            return tip
    except ValueError:
        print("You didn't enter valid cost for the food, please try again")
        return tip_user_input()
