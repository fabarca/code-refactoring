# Based on example_a1.py
import os


def main():
    file_path = "./data/input.csv"
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)
    with open(file_path) as file:
        csv_lines = file.readlines()
    sep = ","
    if len(csv_lines[0].split(sep)) == 0:
        raise ValueError(f"csv_lines is not splittable using sep: '{sep}'")
    csv_dict = {}
    col_names = csv_lines[0].strip("\n").split(sep)
    for col_name in col_names:
        csv_dict[col_name] = []
    csv_dict["total"] = []
    cols_to_sum = ["col2", "col3", "col4"]
    for line in csv_lines[1:]:
        col_num = 0
        line = line.strip("\n")
        row_total = 0
        if len(line) == 0:
            continue
        for column in line.split(sep):
            col_name = col_names[col_num]
            csv_dict[col_name].append(column)
            if col_name in cols_to_sum:
                row_total += float(column)
            col_num += 1
        csv_dict["total"].append(str(row_total))
    print(csv_dict)

main()
