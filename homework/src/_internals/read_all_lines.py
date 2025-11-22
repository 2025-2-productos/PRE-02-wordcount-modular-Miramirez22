import os


def read_all_lines():
    all_lines = []
    input_files_list = os.listdir("data/input/")
    for filename in input_files_list:
        with open(os.path.join("data/input/", filename), "r", encoding="utf-8") as f:
            all_lines.extend(f.readlines())
    return all_lines