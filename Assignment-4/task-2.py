try:
    with open("output.txt", "a") as output:
        output.write(f"{input("Enter text to write to the file: ")}\n")
        print("Data successfully written to output.txt.\n")

        output.write(f"{input("Enter additional text to append: ")}")
        print("Data successfully appended.\n")

    with open("output.txt") as output:
        print("Final content of output.txt")
        print(output.read())

except:
    print("Unexpected error occured.")