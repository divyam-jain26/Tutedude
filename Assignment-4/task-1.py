try:
    with open("sample.txt") as sample:
        print("Reading file content:")
        for num, line in enumerate(sample):
            print(f"Line {num+1}: {line.removesuffix("\n")}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")