def read_file(file_path: str) -> [str]:
    file = None
    try:
        file = open(file_path)
    except OSError:
        print(f"Error! Couldn't open the file at path {file_path}.")
    else:
        lines = []
        for line in file:
            lines.append(line)
        return lines
    finally:
        if file != None:
            file.close()

text = read_file("myfile.txt")

if text != None:
    print(text)
    