def run_grade_tracker():
    # List to store all student records
    all_students = []
    
    print("--- Student Grade Tracker ---")
    print("Type 'exit' as the student name to finish and see the report.\n")

    while True:
        name = input("Enter student name (or type 'exit'): ").strip()
        
        # Check for exit condition
        if name.lower() == 'exit':
            break
            
        try:
            m1 = float(input(f"Enter marks for {name}'s Subject 1: "))
            m2 = float(input(f"Enter marks for {name}'s Subject 2: "))
            m3 = float(input(f"Enter marks for {name}'s Subject 3: "))
            
            avg = (m1 + m2 + m3) / 3
            
            # Grading Logic
            if avg >= 75:
                grade = "A"
                status = "PASS"
            elif avg >= 60:
                grade = "B"
                status = "PASS"
            elif avg >= 40:
                grade = "C"
                status = "PASS"
            else:
                grade = "F"
                status = "FAIL"
            
            # Store student data as a dictionary
            student_data = {
                "name": name,
                "average": round(avg, 2),
                "grade": grade,
                "status": status
            }
            all_students.append(student_data)
            print(f"Data for {name} saved.\n")

        except ValueError:
            print("Invalid input. Please enter numbers for marks. Let's try again.\n")

    # Final Report Display
    if all_students:
        print("\n" + "="*45)
        print(f"{'NAME':<15} | {'AVG':<8} | {'GRADE':<8} | {'STATUS'}")
        print("-" * 45)
        
        for student in all_students:
            print(f"{student['name']:<15} | {student['average']:<8} | {student['grade']:<8} | {student['status']}")
        
        print("="*45)
    else:
        print("\nNo data was entered.")

if __name__ == "__main__":
    run_grade_tracker()