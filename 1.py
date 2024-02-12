number = []

while True:
    r = input("Input a numerical value or simply hit Enter to exit: ")
    if r == "":
        break
    number.append(int(r))

number.sort(reverse=True)

print("five greatest numbers in descending order are:")
for number in number [:5]:
 print(number)