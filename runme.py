from parser import parser

def parse_file(file_path):
    with open(file_path, 'r') as file:
        program = file.read()  
        ast = parser.parse(program)  
        if ast is not None:
            variables = {}
            for statement in ast:  
                statement.evaluate(variables) 

def select_file():
    while True:
        print("Select a file to parse:")
        print("1. Basic Calculator")
        print("2. Boolean Logic")
        print("3. Text Values")
        print("4. Global Data")
        print("5. Control Flow")

        choice = input("Enter a number between 1 and 5: ")
        if choice.isdigit():
            choice = int(choice)
            return choice
        print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    
    print("   _____ _                                                  _   ")
    print("  / ____| |                           /\                   | |  ")
    print(" | (___ | | ___  ___ _ __   ___ _ __ /  \   __ _  ___ _ __ | |_ ")
    print("  \___ \| |/ _ \/ _ \ '_ \ / _ \ '__/ /\ \ / _` |/ _ \ '_ \| __|")
    print("  ____) | |  __/  __/ |_) |  __/ | / ____ \ (_| |  __/ | | | |_ ")
    print(" |_____/|_|\___|\___| .__/ \___|_|/_/    \_\__, |\___|_| |_|\__|")
    print("                    | |                     __/ |               ")
    print("                    |_|                    |___/                ")
    print("                                                                ")
    print("--------------MI5's Favourite Programming Language--------------")
    print("                                                                ")
    
    while True:
        file_path = select_file()
        match file_path:
            case 1:
                file_path = "Example Code/Basic Calculator.txt"
            case 2:
                file_path = "Example Code/Boolean Logic.txt"
            case 3: 
                file_path = "Example Code/Text Values.txt"
            case 4:
                file_path = "Example Code/Global Data.txt"
            case 5:
                file_path = "Example Code/Control Flow.txt"
            case default:
                print("Invalid choice.")
                continue
        parse_file(file_path)
        continue_choice = input("Do you want to parse another file? (y/n): ")
        if continue_choice.lower() != 'y':
            exit(0)