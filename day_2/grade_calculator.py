def calculate_results():
    # Get student details
    name = input("Enter student name: ")
    
    try:
        # Get marks for 3 subjects
        m1 = float(input("Enter marks for Subject 1: "))
        m2 = float(input("Enter marks for Subject 2: "))
        m3 = float(input("Enter marks for Subject 3: "))
        
        # Calculate average
        average = (m1 + m2 + m3) / 3
        
        # Display results
        print(f"\n--- Results for {name} ---")
        print(f"Average Marks: {average:.2f}")
        
        if average >= 40:
            print("Status: PASS")
        else:
            print("Status: FAIL")
            
    except ValueError:
        print("Invalid input! Please enter numerical values for marks.")

if __name__ == "__main__":
    calculate_results()