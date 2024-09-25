import random  # Make sure to import random

def enhancePassword(pword):
    pword = replaceWithNumber(pword)
    pword = replaceWithUppercaseLetter(pword)
    return pword

def replaceWithNumber(pword):
    pword = list(pword)  # Convert string to list for easier manipulation
    for _ in range(random.randrange(1, 3)):  # Randomly replace 1-2 characters with numbers
        replace_index = random.randrange(len(pword))
        pword[replace_index] = str(random.randrange(10))
    return ''.join(pword)

def replaceWithUppercaseLetter(pword):
    pword = list(pword)
    for _ in range(random.randrange(1, 3)):  # Randomly replace 1-2 characters with uppercase letters
        replace_index = random.randrange(len(pword))
        pword[replace_index] = pword[replace_index].upper()
    return ''.join(pword)

def main():
    numPasswords = int(input("How many passwords do you want to input? "))
    
    passwords = []
    
    for i in range(numPasswords):
        password = input(f"Enter password #{i+1}: ")
        
        if len(password) < 3:
            print("Password is too short. Minimum length is 3. Adding default padding.")
            password = password.ljust(3, '*')  # Padding password with '*' to meet minimum length
        
        enhance_choice = input("Do you want to enhance your password (add numbers/uppercase)? (yes/no): ").lower()
        
        if enhance_choice == 'yes':
            password = enhancePassword(password)
        
        passwords.append(password)
    
    for i, password in enumerate(passwords, 1):
        print(f"Password #{i}: {password}")

main()
