def calculate_graded_results():
    name = input("Enter student name: ")
    
    try:
        m1 = float(input("Enter marks for Subject 1: "))
        m2 = float(input("Enter marks for Subject 2: "))
        m3 = float(input("Enter marks for Subject 3: "))
        
        average = (m1 + m2 + m3) / 3
        
        # Grading Logic
        if average >= 75:
            grade = "A"
            status = "PASS"
        elif average >= 60:
            grade = "B"
            status = "PASS"
        elif average >= 40:
            grade = "C"
            status = "PASS"
        else:
            grade = "N/A"
            status = "FAIL"
            
        print(f"\n--- Results for {name} ---")
        print(f"Average: {average:.2f}")
        print(f"Grade:   {grade}")
        print(f"Status:  {status}")
            
    except ValueError:
        print("Error: Please enter numbers for the marks.")

if __name__ == "__main__":
    calculate_graded_results()