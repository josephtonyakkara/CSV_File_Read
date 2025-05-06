import csv
import os

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
            return total / count
        else:
            return 0  # Return 0 if the file is empty or no valid data is found
    except FileNotFoundError:
        print(f"Error: File not found at {filename}")
        return 0
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
        return 0
def get_csv_averages(folder_path):
    """
    Calculates the average of the first column for each CSV file in a folder.

    Args:
        folder_path (str): The path to the folder containing the CSV files.

    Returns:
        dict: A dictionary where keys are CSV filenames and values are the averages.
             Returns an empty dictionary if no CSV files are found or an error occurs.
    """
    averages = {}
    try:
        # Get a list of all files in the folder
        files = os.listdir(folder_path)
        for file in files:
            
            if file.lower().endswith(".csv"):  # Check if the file is a CSV file
                file_path = os.path.join(folder_path, file)  # Construct the full file path
                average = average_of_first_column(file_path)
                if average != 0:
                  averages[file] = average  # Add the filename and average to the dictionary
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
        for filename, average in file_averages.items():
            print(f"{filename}: {average}")
    else:
        print(f"No CSV files found in the specified folder or error occurred.")

