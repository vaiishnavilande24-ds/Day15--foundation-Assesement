
import csv

try:
    # 1. Create and write a text file
    with open("student.txt", "w") as file:
        file.write("Welcome to Python File Handling\n")
        file.write("Name: Priya\n")
        file.write("Marks: 90\n")

    print("Text file written successfully!")

    # 2. Read text file
    with open("student.txt", "r") as file:
        print("\nReading Text File:")
        print(file.read())

    # 3. Append data to text file
    with open("student.txt", "a") as file:
        file.write("Course: Data Analytics\n")

    print("Data appended successfully!")

    # 4. Read file line by line
    with open("student.txt", "r") as file:
        print("\nReading Line by Line:")
        for line in file:
            print(line.strip())

    # 5. Write data into CSV file
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["ID", "Name", "Marks"])
        writer.writerow([1, "Priya", 90])
        writer.writerow([2, "Rahul", 85])
        writer.writerow([3, "Amit", 78])

    print("\nCSV file written successfully!")

    # 6. Read CSV file
    with open("students.csv", "r", newline="") as file:
        reader = csv.reader(file)

        print("\nReading CSV File:")
        for row in reader:
            print(row)

    # 7. Handle user input errors
    try:
        num = int(input("\nEnter a number: "))
        result = 100 / num
        print("Result:", result)

    except ValueError:
        print("Error: Please enter a valid number.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    else:
        print("Calculation completed successfully.")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except OSError as e:
    print("File operation error:", e)

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("\nProgram execution completed.")
