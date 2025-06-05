

print("Please enter your name")
name = input()
print("Please enter your favorite color")
favorite_color = input()

with open("./name_list.txt", "a") as names:
   names.write(f"{name} - {favorite_color}\n")
