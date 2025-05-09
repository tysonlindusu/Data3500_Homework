user_age = input("What is your age?")
desired_life_expectancy = input("What age would you like to live to?")
remaining_life = eval(desired_life_expectancy) - eval(user_age)
print("""If your plan goes well, then you'll still be with us for another """,remaining_life, """ years!""")