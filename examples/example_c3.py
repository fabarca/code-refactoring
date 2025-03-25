"""
Based on example_b2.py

Cognitive Complexity: 11

Changes:
- apply separation of concerns:
    - read file
    - parse csv lines to a dict
    - process csv dict

Notes:
- Cognitive complexity metric didn't change, but the code now is easier to read because steps are explicitly separated

"""

import os


def main():
    # Read file
    file_path = "./data/input.csv"
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)
    with open(file_path) as file:
        csv_lines = file.readlines()

    # Parse CSV lines
    sep = ","
    if len(csv_lines[0].split(sep)) == 0:
        raise ValueError(f"csv_lines is not splittable using sep: '{sep}'")
    csv_dict = {}
    col_names = csv_lines[0].strip("\n").split(sep) # parse CSV header
    for col_name in col_names:
        csv_dict[col_name] = []

    for line in csv_lines[1:]:  # parse CSV rows
        col_num = 0
        line = line.strip("\n")
        if len(line) == 0:
            continue
        for column in line.split(sep):
            col_name = col_names[col_num]
            csv_dict[col_name].append(column)
            col_num += 1

    # Process CSV dict
    cols_to_sum = ["col2", "col3", "col4"]
    csv_dict["total"] = [0] * len(csv_dict[cols_to_sum[0]])
    for col_name in cols_to_sum:
        row_num = 0
        for row_value in csv_dict[col_name]:
            csv_dict["total"][row_num] += float(row_value)
            row_num += 1

    print(csv_dict)

main()
