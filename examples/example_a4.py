"""
Based on example_a3.py

Cognitive Complexity: 7

Changes:
- move code that parse the lines of csv from parse_csv() to parse_csv_line_to_dict()

Notes:
- The separation of the code that parse the lines seems artificial:
    - it needs a several arguments
    - it needs to mutate a dictonary in place without return

"""

import os


def parse_csv_line_to_dict(csv_dict, line, line_num, col_names, sep, cols_to_sum):
    col_num = 0
    row_total = 0
    for column in line.split(sep):
        if line_num == 0:
            csv_dict[column] = []
            col_names.append(column)
            continue
        col_name = col_names[col_num]
        csv_dict[col_name].append(column)
        if col_name in cols_to_sum:
            row_total += float(column)
        col_num += 1
    if line_num == 0:
        csv_dict["total"] = []
    else:
        csv_dict["total"].append(str(row_total))


def parse_csv(csv_lines, sep, cols_to_sum):
    csv_dict = {}
    line_num = 0
    col_names = []
    for line in csv_lines:
        line = line.strip("\n")
        if len(line) > 0:
            parse_csv_line_to_dict(csv_dict, line, line_num, col_names, sep, cols_to_sum)
        line_num += 1

    return csv_dict


def get_csv_dict_with_total(file_path, sep, cols_to_sum):
    csv_dict = {}
    with open(file_path) as file:
        csv_lines = file.readlines()
        if len(csv_lines[0].split(sep)) > 1:
            csv_dict = parse_csv(csv_lines, sep, cols_to_sum)
        else:
            raise ValueError(f"csv_lines is not splittable using sep: '{sep}'")
    return csv_dict


def main():
    file_path = "./data/input.csv"
    sep = ","
    cols_to_sum = ["col2", "col3", "col4"]
    if os.path.exists(file_path):
        csv_dict = get_csv_dict_with_total(file_path, sep, cols_to_sum)
        print(csv_dict)
    else:
        raise FileNotFoundError(file_path)

main()
