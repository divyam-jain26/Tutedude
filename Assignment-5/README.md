# Task 1
**Functionality of the Program**

This program **retrieves and displays a student’s marks from a dictionary** based on user input. Its functionality is:

1. A **dictionary `std_marks`** is defined, where:

   * Keys represent **student names**.
   * Values represent their **marks**.
2. The program uses a **`try` block** to handle unexpected runtime errors.
3. It **takes a student’s name as input** from the user and applies `.capitalize()`:

   * This ensures the name format matches the dictionary keys (first letter uppercase).
4. It **checks whether the entered name exists** in the dictionary:

   * If found, it **prints the student’s marks**.
   * If not found, it prints **"Student not found."**
5. If any **unexpected error** occurs during execution, the `except` block prints an error message.

**In summary:**
The program allows the user to enter a student’s name and displays the corresponding marks if the student exists in the record, while handling unexpected errors gracefully.

# Task 2
**Functionality of the Program**

This program **demonstrates list slicing and list reversal**. Its functionality is:

1. It defines a list `og` containing numbers from **1 to 10**.
2. It **extracts the first five elements** of the list using slicing (`og[:5]`) and stores them in `five`.
3. It **reverses the extracted list** using slicing with a negative step (`five[::-1]`) and stores the result in `rev`.
4. It **prints**:

   * The original list.
   * The first five extracted elements.
   * The reversed version of those extracted elements.

**In summary:**
The program shows how to **slice a list**, **reverse a list using slicing**, and display the results clearly.
