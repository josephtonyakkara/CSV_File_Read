
import csv
print("HI")

def average_of_first_column(filename):
    """
    Calculates the average of the values in the first column of a CSV file.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        float: The average of the values in the first column.
               Returns 0 if the file is empty or an error occurs.
    """
    total = 0
    count = 0
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            header = next(reader)  # Skip the header row
            for row in reader:
                try:
                    value = float(row[0])  # Convert the first value to a float
                    total += value
                    count += 1
                except ValueError:
                    print(f"Skipping invalid data: {row[0]} in file {filename}") # print the invalid data
                    pass  # Skip rows where the first value is not a valid number

        if count > 0:
            return total / count
        else:
            return 0  # Return 0 if the file is empty or no valid data is found
    except FileNotFoundError:
        print(f"Error: File not found at {filename}")
        return 0
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
        return 0

if __name__ == "__main__":
    csv_file = "TOnTOff_20250505140151.csv"  # Replace with the actual path to your CSV file
    average = average_of_first_column(csv_file)
    if average !=0:
      print(f"The average of the first column in '{csv_file}' is: {average}")
    else:
       print(f"No valid data found in the first column of '{csv_file}' .")
