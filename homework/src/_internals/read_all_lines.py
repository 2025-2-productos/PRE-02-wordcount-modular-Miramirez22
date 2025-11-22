import os


def read_all_lines(input_folder):
    all_lines = []
    input_files_list = os.listdir(input_folder)
    for filename in input_files_list:
        with open(os.path.join(input_folder, filename), "r", encoding="utf-8") as f:
            all_lines.extend(f.readlines())
    return all_lines