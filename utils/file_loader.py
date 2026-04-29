import os

def load_code_files(path):
    code_files = {}

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                with open(full_path, "r", encoding="utf-8") as f:
                    code_files[full_path] = f.read()

    return code_files
