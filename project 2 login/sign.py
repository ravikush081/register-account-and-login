from asyncio.constants import FLOW_CONTROL_HIGH_WATER_SSL_READ
import os  # <-- नई लाइन: file check करने के लिए
import getpass
import re
# अगर file नहीं है तो बना दो
if not os.path.exists("password.txt"):
    with open("password.txt", "w") as f:
        f.write("FirstName,SecondName,Age,Gender,Mobile,Gmail,Password\n")  # header डालना optional है

while True:
    name = input("Enter a first name: ")
    if name.isalpha():
        break
    else:
        print("Invalid input! Please enter a valid first name.")

while True:
    name2 = input("Enter a second name: ")
    if name2.isalpha():
        break
    else:
        print("Invalid input! Please enter a valid second name.")

while True:
    age = input("Enter your age: ")
    if age.isdigit():
        break
    else:
        print("Invalid input! Please enter a valid age.")

while True:
    print("Enter your gender (1)Male (2)Female (3)Transgender")
    gander = input("Choose option 1, 2, or 3: ")
    if gander.isdigit():
        gander = int(gander)
        if gander in [1, 2, 3]:
            break
        else:
            print("Invalid input! Select only 1, 2, or 3.")
    else:
        print("Invalid input! Please select only 1, 2, or 3.")

while True:
    mobile = input("Enter a mobile number: ")
    if not (mobile.isdigit() and len(mobile) == 10):
        print("Invalid input! Please enter a 10-digit number.")
        continue

    found = False
    with open('password.txt', 'r') as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) > 4 and parts[4] == mobile:
                print("Your number already exists.")
                found = True
                break

    if found:
        continue
    else:
        break

while True:
    gmail = input("Enter your Gmail ID: ")
    if not (gmail.lower().endswith("@gmail.com") and len(gmail) > 10):
        print("Invalid input! Enter a valid Gmail ID.")
        continue

    found = False
    with open('password.txt', 'r') as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) > 5 and parts[5] == gmail:
                print("Your Gmail already exists.")
                found = True
                break

    if found:
        continue
    else:
        break

while True:
    password = input(("Enter a strong password (min 8 chars, upper, lower, digit, special): "))

    if len(password) < 8:
        print(" Password must be at least 8 characters long.")
    elif not re.search("[A-Z]", password):
        print(" Must include at least one uppercase letter.")
    elif not re.search("[a-z]", password):
        print(" Must include at least one lowercase letter.")
    elif not re.search("[0-9]", password):
        print(" Must include at least one digit.")
    elif not re.search("[@#$%^&+=!]", password):
        print(" Must include at least one special character (@, #, $, etc.).")
    else:
        print("Strong password accepted.")
        break


ga = ["Male", "Female", "Transgender"]
gandersavefile = ga[gander - 1]

with open('password.txt', 'a') as f:
    f.write(f"{name},{name2},{age},{gandersavefile},{mobile},{gmail},{password}\n")

print("\n✅ Thanks for creating an account!\n")
print("Your First Name:     ", name)
print("Your Second Name:    ", name2)
print("Your Age:            ", age)
print("Your Gender:         ", gandersavefile)
print("Your Mobile Number:  ", mobile)
print("Your Gmail:          ", gmail)
print("\nNow you can login to your account!\n")
