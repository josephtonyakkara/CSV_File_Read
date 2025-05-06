import csv
import os

def average_of_first_column(filename):
    """
    Calculates the average of the values in the first column of a CSV file.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        tuple: (average, values_in_range)
            - average: The average of the values in the first column.
                       Returns 0 if the file is empty or an error occurs.
            - values_in_range: A list of values from the first column that are
                               within 100 of the average (inclusive).
    """
    total = 0
    count = 0
    values_in_range = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=';')  # Specify the delimiter as a semicolon
            header = next(reader)  # Skip the header row
            for row in reader:
                try:
                    value = float(row[0])  # Convert the first value to a float
                    total += value
                    count += 1
                except ValueError:
                    print(f"Skipping invalid data: {row[0]} in file {filename}")
                    pass  # Skip rows where the first value is not a valid number

        if count > 0:
            average = total / count
            print(average)
            for row in csv.reader(open(filename, 'r'), delimiter=';'):
                try:
                    value = float(row[0])
                    if (value <= average - 2000 or value >= average + 1000):
                        print(value)
                        values_in_range.append(value)
                except ValueError:
                    pass
            return average, values_in_range
        else:
            return 0, []  # Return 0 and empty list if no valid data
    except FileNotFoundError:
        print(f"Error: File not found at {filename}")
        return 0, []
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
        return 0, []


def get_csv_averages(folder_path):
    """
    Calculates the average of the first column for each CSV file in a folder.

    Args:
        folder_path (str): The path to the folder containing the CSV files.

    Returns:
        dict: A dictionary where keys are CSV filenames and values are dictionaries
              containing the average and values within 100 of the average.
              Returns an empty dictionary if no CSV files are found or an error occurs.
    """
    averages = {}
    try:
        # Get a list of all files in the folder
        files = os.listdir(folder_path)
        for file in files:
            if file.lower().endswith(".csv"):  # Check if the file is a CSV file
                file_path = os.path.join(folder_path, file)  # Construct the full file path
                average, values_in_range = average_of_first_column(file_path)
                if average != 0:
                    averages[file] = {
                        "average": average,
                        "values_in_range": values_in_range
                    }  # Store both average and values
                else:
                    print(f"No valid data found in the first column of '{file_path}' .")
        return averages
    except FileNotFoundError:
        print(f"Error: Folder not found at {folder_path}")
        return {}
    except Exception as e:
        print(f"An error occurred while processing the folder: {e}")
        return {}


if __name__ == "__main__":
    folder_path = "./test_data/"  # Replace with the actual path to your folder containing CSV files
    file_averages = get_csv_averages(folder_path)
    if file_averages:
        print("Average of the first column for each CSV file:")
        for filename, data in file_averages.items():
            print(f"{filename}: Average = {data['average']:.2f}, Values outside range = {data['values_in_range']}")
    else:
        print(f"No CSV files found in the specified folder or error occurred.")
