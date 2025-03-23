import os

class CsvParserWithTotal:
    def __init__(self, file_path, sep, cols_to_sum):
        self.file_path = file_path
        self.sep = sep
        self.cols_to_sum = cols_to_sum
        self.csv_dict = {}
        self.line_num = 0
        self.col_names = []

    def parse_csv_line_to_dict(self, line):
        col_num = 0
        row_total = 0
        for column in line.split(self.sep):
            if self.line_num == 0:
                self.csv_dict[column] = []
                self.col_names.append(column)
                continue
            col_name = self.col_names[col_num]
            self.csv_dict[col_name].append(column)
            if col_name in self.cols_to_sum:
                row_total += float(column)
            col_num += 1
        if self.line_num == 0:
            self.csv_dict["total"] = []
            self.line_num += 1
            return
        self.csv_dict["total"].append(str(row_total))

    def parse_csv(self, csv_lines):
        self.line_num = 0
        self.col_names = []
        for line in csv_lines:
            line = line.strip("\n")
            if len(line) > 0:
                self.parse_csv_line_to_dict(line)

    def get_csv_dict_with_total(self):
        with open(self.file_path) as file:
            csv_lines = file.readlines()
            if len(csv_lines[0].split(self.sep)) > 1:
                self.parse_csv(csv_lines)
        return self.csv_dict

def main():
    file_path = "./data/input.csv"
    sep = ","
    cols_to_sum = ["col2", "col3", "col4"]
    if os.path.exists(file_path):
        csv_parser = CsvParserWithTotal(file_path, sep, cols_to_sum)
        csv_dict = csv_parser.get_csv_dict_with_total()
        print(csv_dict)

main()
