import csv, ast
from datetime import datetime

class HistorFileManager:
    def __init__(self) -> None:
        self.file_path = "history/history.csv"
        self.MAX_READ = 5
        self.MAX_SAVE = 10

    def save_history(self, path, cost, status):
        # Read existing data from the file
        existing_data = self.read_data(self.file_path)
        path = list(ast.literal_eval(path))
        print("Path: ", path)
        src = path[0]
        des = path[-1]
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime('%d/%m/%Y - %H:%M')

        new_row = [src, des, cost, path, formatted_date, status]
        
        # Append new data to existing data
        all_data = existing_data + [new_row]

        # Write all data back to the file
        self.write_data(self.file_path, all_data)

        data_after_inserted = self.read_history()
        # print("Data after inserted")
        # for row in data_after_inserted:
        #     print(row)
        print("You have added data")
        print(new_row)

    def read_history(self):
        history = self.read_data(self.file_path, read=True)
        return history

    def read_data(self, file_path, read=False):
        """
        Note
        1. config read = True when reading the data
        2. config read = False when writing the data
        """
        if read:
            max_rows = self.MAX_READ + 1 
        else:
            max_rows = self.MAX_SAVE
        data = []
        try:
            with open(file_path, 'r', newline='') as file:
                # Read the last `max_rows` lines from the file
                lines = file.readlines()[-max_rows+1:]
                reader = csv.reader(lines)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        return data

    def write_data(self, file_path, data):
        try:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                for row in data:
                    writer.writerow(row)
        except IOError:
            print(f"Error writing to file: {file_path}")
            print(f"{file_path} created")
