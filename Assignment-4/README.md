# Task 1
**Functionality of the Program**

This program **reads and displays the contents of a text file with error handling**. Its functionality is:

1. It uses a **`try` block** to safely handle file operations.
2. It attempts to **open the file `sample.txt` in read mode** using a `with` statement:

   * This ensures the file is **automatically closed** after use.
3. It prints a heading: `"Reading file content:"`.
4. It **iterates over each line in the file** using `enumerate()`:

   * `num` gives the line index (starting from 0).
   * `line` contains the content of each line.
5. For each line, it:

   * Removes the trailing newline character using `removesuffix("\n")`.
   * Prints the line number (starting from 1) along with the line content.
6. If the file does **not exist**, the `FileNotFoundError` is caught:

   * A clear error message is displayed instead of crashing the program.

**In summary:**
The program reads a text file line by line, prints each line with its line number, and gracefully handles the case where the file is missing.

# Task 2
**Functionality of the Program**

This program **writes data to a file, appends additional data, and then reads the file content**, with basic error handling. Its functionality is:

1. The program uses a **`try` block** to handle any runtime errors that may occur during file operations.
2. It opens the file **`output.txt` in append mode (`"a"`)**:

   * If the file does not exist, it is **created automatically**.
3. It **takes user input** and:

   * Writes the first input followed by a newline to the file.
   * Displays a confirmation message.
4. It takes **another user input** and:

   * Appends it to the same file (without adding a newline).
   * Displays a confirmation message.
5. The file is automatically **closed after writing** due to the `with` statement.
6. The program then **reopens `output.txt` in read mode**:

   * Reads and prints the **entire content of the file**.
7. If **any unexpected error** occurs during execution, the `except` block runs and displays an error message.

**In summary:**
The program appends user-provided text to a file, confirms successful writing, then reads and displays the final contents of the file while handling unexpected errors gracefully.
