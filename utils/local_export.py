import csv
import os

def save_to_csv(filename, row, headers=None):
    path = os.path.join("results", filename)
    write_headers = not os.path.exists(path)
    with open(path, mode='a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        if write_headers:
            writer.writerow(headers)
        writer.writerow(row)