# import custom helper functions
from tip_calculator_helpers import *

# main function
def tip_calculator():
    # 'its_go_time' is the conditon for the while loop. At the end of the tip calculation the user is asked it they want to continue
    its_go_time = 'yes'
    
    # while will contiune to run as long as the user wants
    while its_go_time.lower() == 'yes':
        # variables used in the function
        cost = cost_of_food_user_input()
        number_of_people = number_of_people_user_input()
        tip = tip_user_input(cost)
        tax = cost * .1
        total_cost = cost

        # if there is a tip add it and the tax else just add tax
        if tip:
            total_cost = total_cost * (1 + tip/100) + tax
        else:
            total_cost = total_cost + tax

        # print total bill to user
        if cost:
            print(f"Total bill: {'{:.2f}'.format(total_cost)}")

        # if number of people is greater than 1 display cost each person will pay
        if number_of_people > 1:
            print(f"Each person should pay ${'{:.2f}'.format(total_cost / number_of_people)}")

        # asking if user want to use the tip calculator again
        its_go_time = input('Please enter Yes to calculate another tip or enter No to stop ')

tip_calculator()

# https://www.revenue.wi.gov/Pages/TaxPro/2014/news-2014-140213.aspx#:~:text=Since%20the%20tip%20is%20wholly,by%20Restaurant%20to%20the%20bill.