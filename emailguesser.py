import os
import subprocess
from datetime import datetime

def generate_email_combinations(name, surname, domain):
    """
    Generate a list of possible email combinations based on the given name, surname, and domain.
    """
    combinations = set()
    
    # Add basic combinations
    combinations.add(f"{name}@{domain}")
    combinations.add(f"{name[:3]}@{domain}")
    combinations.add(f"{surname}@{domain}")
    combinations.add(f"{surname[:3]}@{domain}")
    
    for sep in ["", ".", "-"]:
        # Name first combinations
        combinations.add(f"{name}{sep}{surname}@{domain}")
        combinations.add(f"{name[0]}{sep}{surname}@{domain}")
        for i in range(1, 4):
            combinations.add(f"{name[0]}{sep}{surname[:i]}@{domain}")
        for i in range(1, 3):
            combinations.add(f"{name[:i]}{sep}{surname[0]}@{domain}")
        
        # Surname first combinations
        combinations.add(f"{surname}{sep}{name}@{domain}")
        combinations.add(f"{surname[0]}{sep}{name}@{domain}")
        for i in range(1, 4):
            combinations.add(f"{surname[0]}{sep}{name[:i]}@{domain}")
        for i in range(1, 3):
            combinations.add(f"{surname[:i]}{sep}{name[0]}@{domain}")
    
    unique_combinations = sorted(combinations)
    
    return unique_combinations

def display_combinations(combinations):
    """
    Display the email combinations in the console.
    """
    print(f"Total combinations: {len(combinations)}")
    print(", ".join(combinations))

def save_combinations_to_file(combinations):
    """
    Save the email combinations to a file and open the file in the default text editor.
    """
    timestamp = datetime.now().strftime("%H-%M_%d_%m_%y")  # Replace colons with hyphens
    filename = f"emails_{timestamp}.txt"
    try:
        with open(filename, 'w') as file:
            file.write(f"Total combinations: {len(combinations)}\n")
            file.write(", ".join(combinations))
        full_path = os.path.abspath(filename)
        print(f"Combinations saved to {full_path}")
        
        # Open the file in the default text editor
        if os.name == 'nt':  # For Windows
            os.startfile(full_path)
        elif os.name == 'posix':  # For macOS and Linux
            subprocess.run(['open', full_path] if sys.platform == 'darwin' else ['xdg-open', full_path])
    except Exception as e:
        print(f"Error saving combinations to file: {e}")

def get_user_input():
    """
    Get user input for name, surname, and domain.
    """
    while True:
        user_input = input("Enter the first name, surname, and domain (comma-separated or space-separated) or press Enter to input separately: ").strip()
        
        if user_input:
            try:
                if ',' in user_input:
                    name, surname, domain = [x.strip() for x in user_input.split(',')]
                else:
                    name, surname, domain = [x.strip() for x in user_input.split()]
                if not name or not surname or not domain:
                    raise ValueError
                return name, surname, domain
            except ValueError:
                print("Invalid input format. Please enter the values as 'name, surname, domain' or 'name surname domain'.")
        else:
            name = input("Enter the first name: ").strip()
            surname = input("Enter the surname: ").strip()
            domain = input("Enter the domain without @ symbol: ").strip()
            if name and surname and domain:
                return name, surname, domain
            else:
                print("All fields are required. Please try again.")

def handle_output_choice(combinations):
    """
    Handle the user's choice for output (console or file).
    """
    while True:
        output_choice = input("Do you want to display the results in the console or save to a file? (C/F): ").strip().lower()
        if output_choice == "c":
            display_combinations(combinations)
            input("Press Enter to exit...")
            break
        elif output_choice == "f":
            save_combinations_to_file(combinations)
            break
        else:
            print("Invalid choice. Please enter 'C' for a console output OR 'F' for a file output.")

def main():
    """
    Main function to run the email guesser script.
    """
    while True:
        name, surname, domain = get_user_input()
        if not name or not surname or not domain:
            continue
        
        combinations = generate_email_combinations(name, surname, domain)
        handle_output_choice(combinations)

if __name__ == "__main__":
    main()
