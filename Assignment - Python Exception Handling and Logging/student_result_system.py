import logging


logging.basicConfig(
    filename="student_app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def calculate_average(marks):
    """Return the average of a list of marks."""
    try:
        return sum(marks) / len(marks)
    except ZeroDivisionError:
        logging.error("Cannot calculate average: no subjects/marks available.")
        raise


def get_result(average):
    """Return the result category based on the average."""
    if 90 <= average <= 100:
        return "Excellent"
    elif 75 <= average < 90:
        return "Very Good"
    elif 50 <= average < 75:
        return "Pass"
    return "Fail"


def get_number_of_subjects():
    """Read and validate the number of subjects."""
    while True:
        try:
            number = int(input("Enter number of subjects: "))
        except ValueError:
            print("Please enter a valid number.")
            logging.error("Invalid number of subjects entered.")
        else:
            logging.debug("Number of subjects entered: %d", number)
            return number


def get_marks(number_of_subjects):
    """Read and validate marks for each subject."""
    marks = []

    for subject in range(1, number_of_subjects + 1):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {subject}: "))

                if not 0 <= mark <= 100:
                    raise ValueError("Marks must be between 0 and 100.")

            except ValueError as exc:
                print("Marks must be between 0 and 100." if "between" in str(exc)
                      else "Please enter a valid mark.")
                logging.error("Invalid marks entered for subject %d: %s", subject, exc)
            else:
                marks.append(mark)
                logging.info("Mark entered successfully for subject %d: %.2f", subject, mark)

                if mark < 50:
                    logging.warning("Mark for subject %d is below passing range: %.2f", subject, mark)
                elif mark < 55:
                    logging.warning("Mark for subject %d is close to the minimum passing mark: %.2f", subject, mark)
                break

    return marks


def process_student():
    """Process one student's result."""
    logging.info("Student processing started.")

    try:
        student_name = input("Enter student name: ").strip()
        logging.info("Student name received.")

        number_of_subjects = get_number_of_subjects()

        if number_of_subjects < 0:
            print("Number of subjects cannot be negative.")
            logging.error("Negative number of subjects entered: %d", number_of_subjects)
            return True

        if number_of_subjects == 0:
            # Intentionally allow zero so the required ZeroDivisionError
            # handling can be demonstrated in calculate_average().
            logging.warning("Student entered 0 subjects.")

        marks = get_marks(number_of_subjects)
        logging.info("Marks entered successfully.")

        try:
            average = calculate_average(marks)
        except ZeroDivisionError:
            print("Cannot calculate the average because the number of subjects is zero.")
            logging.error("Student processing stopped due to division by zero.")
            return True
        else:
            logging.info("Average calculation completed: %.2f", average)

        result = get_result(average)
        logging.info("Result determined: %s", result)

        print("\n----- Student Result -----")
        print(f"Student Name : {student_name}")
        print(f"Average : {average:.2f}")
        print(f"Result : {result}")

        # Bonus task: statistics.
        if marks:
            highest = max(marks)
            lowest = min(marks)
            print("\n----- Student Statistics -----")
            print(f"Highest Mark : {highest:g}")
            print(f"Lowest Mark : {lowest:g}")
            print(f"Average Mark : {average:.2f}")
            print(f"Result : {result}")
            logging.info("Student statistics calculated successfully.")

        logging.debug("Completed processing for student: %s", student_name)
        return True

    except KeyboardInterrupt:
        logging.warning("User interrupted the application.")
        print("\nApplication interrupted by user.")
        return False
    except Exception as exc:
        # This is only a final safety net. Specific exceptions are handled
        # above, following the assignment's best-practice guidance.
        logging.critical("Unexpected failure during student processing: %s", exc, exc_info=True)
        print("An unexpected error occurred. Please check the log file.")
        return False
    finally:
        print("Processing completed.")
        logging.info("Student processing completed.")


def main():
    """Run the Student Result Processing System."""
    logging.info("Application started.")

    try:
        while True:
            should_continue = process_student()
            if not should_continue:
                break

            choice = input("\nDo you want to enter another student? (yes/no): ").strip().lower()
            if choice != "yes":
                break

    finally:
        logging.info("Application completed.")
        logging.debug("Final cleanup reached in main().")
        print("Application closed.")


if __name__ == "__main__":
    main()
