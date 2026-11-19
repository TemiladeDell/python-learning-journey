from students import student, student_manager

st = student()
sm = student_manager()

class validate:
    def check():
        search_id = input("Enter the student's ID: ").strip().casefold()
        record = next(
            (
                candidate
                for candidate in sm.students
                if str(getattr(candidate, "Id", "")).casefold() == search_id
            ),
            None,
        )
        if record is None:
            print("Student not found.")
            return

        if record.registration_date is None or record.course_years is None:
            print("Registration date or course period is missing.")
            return

        try:
            course_years = int(record.course_years)
            registration_date = record.registration_date
            expiry_date = registration_date.replace(
                year=registration_date.year + course_years
            )
        except (TypeError, ValueError):
            print("Enter valid numeric course details.")
            return

        today = datetime.now()
        if today >= expiry_date:
            print("This student's course period has expired.")
        else:
            print("This student's course period is still valid.")