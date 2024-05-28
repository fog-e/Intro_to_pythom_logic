i = 0
numbers_divisible_by_3 = 0

while numbers_divisible_by_3 < 10:
    i = i + 1
    if i % 3 == 0:
        numbers_divisible_by_3 = numbers_divisible_by_3 + 1
        print(i)
print(i)

for i in range(0, 10):
    print(i)

my_name = "Liz Howard"

for i in range(len(my_name)):
    print(my_name[i])

names = ["Kellyn", "Max", "Joe", "Roan"]

for name in names:
    print(name + " is RSVP'd")

names = ["Kellyn", "Max", "Joe", "Roan"]

for name in names:
    print(name + "@themultiverse.school")
import random
import string

# Function to randomize the first letter of a name
def randomize_first_letter(name):
    first_letter = random.choice(string.ascii_uppercase)
    return first_letter + name[1:]

# List of guest names
guests = "Ash,Max,Joe,Roan,Caitlin"

# Split the guest names into a list
names = guests.split(",")

# Append additional names
names.append("Liz")
names.append("Liz")

# Print the length of the names list and the first name
print(len(names))
print(names[0])

# Change the name at index 6 to "Kellyn"
names[6] = "Kellyn"

# Randomize the first letter of each name in the names list
randomized_names = [randomize_first_letter(name) for name in names]

# Print the name that was popped from the list
first_person = names.pop(0)
print(first_person)

# Print each name with the domain appended
for name in randomized_names:
    print(name + "@themultiverse.school")
