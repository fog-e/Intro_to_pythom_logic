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
