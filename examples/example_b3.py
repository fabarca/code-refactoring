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
        return
    csv_dict["total"].append(str(row_total))


def main():
    file_path = "./data/input.csv"
    if not os.path.exists(file_path):
        return None
    csv_dict = {}
    with open(file_path) as file:
        csv_content = file.readlines()
    sep = ","
    if len(csv_content[0].split(sep)) == 0:
        return None
    line_num = 0
    col_names = []
    cols_to_sum = ["col2", "col3", "col4"]
    for line in csv_content:
        line = line.strip("\n")
        if len(line) == 0:
            continue
        parse_csv_line_to_dict(csv_dict, line, line_num, col_names, sep, cols_to_sum)
        line_num += 1
    print(csv_dict)

main()
