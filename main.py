# ---------- DATA STORAGE ----------
students = {}
courses = {}
registrations = {}

# ---------- STUDENT MODULE ----------
def add_student():
    sid = input("Enter Student ID: ").strip()

    if sid in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ").strip()
    students[sid] = name
    print("Student added successfully!")


def view_students():
    print("\n--- Student List ---")
    if not students:
        print("No students available.")
        return

    for sid, name in students.items():
        print(f"{sid} - {name}")


# ---------- COURSE MODULE ----------
def add_course():
    cid = input("Enter Course ID: ").strip()

    if cid in courses:
        print("Course already exists!")
        return

    cname = input("Enter Course Name: ").strip()
    courses[cid] = cname
    print("Course added successfully!")


def view_courses():
    print("\n--- Course List ---")
    if not courses:
        print("No courses available.")
        return

    for cid, cname in courses.items():
        print(f"{cid} - {cname}")


# ---------- REGISTRATION MODULE ----------
def register_course():
    sid = input("Enter Student ID: ").strip()
    cid = input("Enter Course ID: ").strip()

    if sid not in students:
        print("Student not found!")
        return

    if cid not in courses:
        print("Course not found!")
        return

    registrations.setdefault(sid, [])

    if cid in registrations[sid]:
        print("Student already registered for this course!")
        return

    registrations[sid].append(cid)
    print("Course registered successfully!")


def view_registrations():
    print("\n--- Registration Details ---")

    if not registrations:
        print("No registrations found.")
        return

    for sid, course_list in registrations.items():
        print(f"Student: {students[sid]} ({sid})")
        for cid in course_list:
            print(f"  -> {courses[cid]} ({cid})")
        print()


# ---------- MAIN MENU ----------
def main():
    while True:
        print("\n===== ERP STUDENT COURSE SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Add Course")
        print("4. View Courses")
        print("5. Register Course")
        print("6. View Registrations")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        match choice:
            case '1':
                add_student()
            case '2':
                view_students()
            case '3':
                add_course()
            case '4':
                view_courses()
            case '5':
                register_course()
            case '6':
                view_registrations()
            case '7':
                print("Exiting system...")
                break
            case _:
                print("Invalid choice!")


# ---------- RUN ----------
if __name__ == "__main__":
    main()

