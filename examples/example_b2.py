import os


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
        col_num = 0
        line = line.strip("\n")
        row_total = 0
        if len(line) == 0:
            continue
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
            line_num += 1
            continue
        csv_dict["total"].append(str(row_total))
    print(csv_dict)

main()
