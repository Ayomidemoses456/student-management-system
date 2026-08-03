students = []

while True:
    
    print("STUDENT MANAGEMENT SYSTEM")
    print("1. Add student")
    print("2. View student")
    print("3. Search student")
    print("4. Delete student")
    print("5. Exit")
    
    option = input("Enter your option:")
    if option == "1":
     print("ADD STUDENT")
     id = input("Enter student's identity no.:")
     name = input("Enter student's full name:")
     age = int(input("Enter student's age:"))
     gender = input("Enter student's gender:")
     course = input("Enter student's course of study:")
     student = {
        "student_id": id,
        "student_name": name,
        "student_age": age,
        "student_gender": gender,
        "course_of_study": course,
     }
     
     students.append(student)
     print("STUDENT ADDED SUCESSFULLY")
    
     repeat_action = input("Do you want to add another student? (yes/no):")
     if repeat_action.lower() == "yes":
        print("ADD STUDENT")
        id = input("Enter student's identity no.:")
        name = input("Enter student's full name:")
        age = int(input("Enter student's age:"))
        gender = input("Enter student's gender:")
        course = input("Enter student's course of study:")
        student = {
            "student_id": id,
            "student_name": name,
            "student_age": age,
            "student_gender": gender,
            "course_of_study": course,
        } 
         
        
    elif option == "2":
     print("VIEW STUDENT")
     
     if len(students)==0:
         print("No student records found")
         
     else:
         for stud in students:
             print("----------------------------")
             print("ID:", stud["student_id"])
             print("Name:", stud["student_name"])
             print("Age:",stud["student_age"])
             print("Gender:", stud["student_gender"])
             print("Course:", stud["course_of_study"])
             print("----------------------------")
             input("press enter to return to menu..")
    
    elif option =="3":
     search = input("enter student_name for search:")   
     found = True  
     for student in students:
         if student ["student_name"] == search:
          print("student found")
         print("id:", student["student_id"])
         print("Name:", student["student_name"])
         print("age:",student["student_age"])
         print("gender:", student["student_gender"])
         print("course:", student["course_of_study"])
         input("press enter to return to menu..")
         found = True
     if found == False:
         print("student not found.")
         input("press enter to return to menu..")
         break
         
    elif option =="4":
        delete =input("Enter course to delete:")
        for student in students:
            if student["course_of_study"] == delete:
                found= True
                students.remove(student)
                print("student removed sucessfully!")
            if found == False:
              print("student doesn't exist")
              input("press enter to return to main menu")
    elif option== "5":
     print("THANK YOU FOR USING THE STUDENT MANAGEMENT SYSTEM")
     break
    