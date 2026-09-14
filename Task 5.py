#Oppgave 5. Directory lister

import os

path = input ("Directory path:")

try:
    items = os.listdir(path)

    print(f"\nContent in '{path}':")
    print("-" * 30)


    for item in items:
        print(f"-{item}")

except FileNotFoundError:
    print("Error: File path does not exist")

except PermissionError:
    print("Error: You do not have permission")

