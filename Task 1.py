#Task 1 - File to list converter


filename = input("Enter filename: ") #Bruker må skrive inn filnavnet

#Filen blir åpnet og lest, strip fjerner mellomrom og linjeskift

try:
    with open(filename, "r") as file: 
        lines = [line.strip() for line in file]

        print(lines)
       
except FileNotFoundError:
    print("Error: File not found.")

#Fant denne except på realpython.com 