# Write a program that asks the user the year they were born. Display a message telling the user what generation they belong to based on the following rules/years
# - Zoomer 1997
# - Millennial 1981
# - Gen X 1965
# - Baby Boomer 1946


# let's start using actual methods/functions to make our code more reusable and clean
def determine_generation(year):
    #create a mapping object
    generational_map = {
        'Zoomer': range(1997,3000),
        'Millennial': range(1981, 1996),
        'Gen X': range(1965, 1980),
        'Baby Boomer': range(1946, 1964)
    }
    #loop through our object to find the correct range
    for generation, year_range in generational_map.items():
        if year in year_range:
            return generation
    return 'Generation before baby boomers'

try:
    #capture birth year and type cast it into an int
    birth_year = int(input('What year were you born?'))
    #call our function and pass it the birth_year var
    generation = determine_generation(birth_year)
    #interpolated string
    print(f'You belong to the {generation} generation. Very cool!')
except ValueError:
    print('That input was not a valid year')