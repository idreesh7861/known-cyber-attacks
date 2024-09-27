import os
attack_list = os.listdir()
f = open("Compile.md", "w")
f.write("# Known Cyber Attacks \n")
f.write("This markdown contains links to descriptions of known cyber attacks. \n")


# Create subheadings
attack_list.remove(".git")
attack_list.remove("compiler.py")
attack_list.remove("Compile.md")
attack_list.remove("README.md")
attack_list.remove("Template")

for attack in attack_list:
    attack_string = attack.replace(" ", "%20")
    f.write("- [" + attack +"](" + attack_string + "/README.md)\n")
