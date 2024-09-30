import os


input_accepted = False
STRIDE_CATEGORIES = ["spoofing", "tampering", "repudiation", "information disclosure", "denial of service", "elevation of privilege"]

while not input_accepted:
    category = input("Please input a STRIDE Category you would like to search for: ").lower()
    if (category in STRIDE_CATEGORIES):
        input_accepted = True    
    else:
        print("Please input a valid category")

attack_list = os.listdir()

attack_list.remove(".git")
attack_list.remove("compiler.py")
attack_list.remove("Compile.md")
attack_list.remove("README.md")
attack_list.remove("Template")
attack_list.remove("searcher.py")

for attack in attack_list:
    attack.replace(" ", "%20")
    attack = attack + ("\README.md")

for attack in attack_list:
    try:
        with open(attack, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if category in line.lower():
                    attack.replace("%20", " ")
                    print("- " + attack + "\n")
    except FileNotFoundError:
        print(f"The file {file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
        input(" dwad ")

input(" dawijdiowa ")