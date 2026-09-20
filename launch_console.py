import sys
import time

def clear_screen():
    # Simple terminal line clearing to keep the layout neat
    print("\n" * 2)

def welcome_sequence():
    print("==================================================")
    print("         🌸  WELCOME TO GABRIELA_OS  🌸         ")
    print("==================================================")
    print("Initializing core modules...")
    time.sleep(0.5)
    print("Loading art archives & scientific data matrices...")
    time.sleep(0.5)
    print("System status: ONLINE.\n")

def main():
    welcome_sequence()
    
    # 1. Ask for the user's name and store it
    user_name = input("Enter operator credentials (Your Name): ").strip()
    if not user_name:
        user_name = "Gabriela"  # Default backup
        
    print(f"\nWelcome back, Commander {user_name}. Terminal authorized.")
    
    # 2. Main operational menu loop
    while True:
        print("\n" + "="*40)
        print(f" MAIN MENU // AUTH: {user_name.upper()}")
        print("="*40)
        print("[1] About Me")
        print("[2] My Goals")
        print("[3] View Arts & Lit Vault (Custom Option!)")
        print("[4] Exit Terminal")
        print("-"*40)
        
        choice = input("Select a matrix vector [1-4]: ").strip()
        clear_screen()
        
        if choice == "1":
            print("--- MODULE: ABOUT ME ---")
            print("• Aesthetic: Absolutely loves the color pink!")
            print("• Literature: Devoted fan of classic literature works.")
            print("• Creative: Deeply passionate about exploring the fine arts.")
            
        elif choice == "2":
            print("--- MODULE: TARGET GOALS ---")
            print("• Code: Learn modern programming structures and paradigms.")
            print("• Immunology: Master the intricacies of human cell defenses.")
            print("• Pharmacology: Analyze biochemical drug reactions and vectors.")
            
        elif choice == "3":
            print("--- MODULE: ARTS & LIT VAULT ---")
            print("🌸 Fun Fact: Did you know that the color pink was highly prized")
            print("   in 18th-century art to showcase luxury and high fashion?")
            print("\n📚 Current Reading Queue Recommendation:")
            print("   'Frankenstein' by Mary Shelley — the perfect crossover")
            print("   between classic literature and experimental biology!")
            
        elif choice == "4":
            print(f"Deauthorizing session... Goodbye, {user_name}! Have a wonderful day. 🌸")
            print("Closing all connection matrices safely.")
            sys.exit()
            
        else:
            print("⚠️ INVALID INPUT. Please input a number from 1 to 4.")

if __name__ == "__main__":
    main()
