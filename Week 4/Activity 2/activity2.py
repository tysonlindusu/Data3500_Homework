"""
Programming Activity 2 

Update the loop in activity 1 to not only iterate through the colors in the list, but also iterate through each character in each string.
- Nested for loop, to iterate through the characters in each color.
"""
#list (array) of colors
colors = ['grey', 'black', 'white']
#print them using a for loop, but use a nested loop to print each character separately
for i in colors:
    for j in i:
        print(j)