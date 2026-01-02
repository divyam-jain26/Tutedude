# Calculator
**Functionality of the Program**

This program creates a **graphical calculator application** using Python’s **Tkinter** library. Its functionality can be understood in layers: window setup, logic, and user interaction.

At the start, a **GUI window** is created with a fixed size and titled *Calculator*. Resizing is disabled to keep the layout stable and predictable.

The calculator works by maintaining a **global expression string** that represents whatever the user has typed (numbers and operators). This expression is continuously updated and displayed in an entry field at the top of the window.

Three core functions drive the calculator’s behavior:

* **Button Click (`btn_click`)**
  When a number or operator button is pressed, its value is converted to a string and appended to the current expression. The display updates instantly to reflect the new expression.

* **Clear (`btn_clear`)**
  This function resets the expression to an empty string and clears the display, effectively restarting the calculation.

* **Equal (`btn_equal`)**
  This evaluates the mathematical expression using `eval()`.

  * If the expression is valid, the result is shown.
  * If an error occurs (such as division by zero or an invalid expression), `"Error"` is displayed.
    After evaluation, the expression is cleared for the next calculation.

The **user interface** consists of:

* An **input display field** that shows the current expression and result.
* A **grid of buttons** for digits (0–9), arithmetic operators (`+`, `-`, `*`, `/`), a decimal point, clear (`C`), and equals (`=`).

Each button is linked to its corresponding function using `command`, allowing real-time interaction.

Finally, `mainloop()` keeps the window running and responsive until the user closes it.

**In summary:**
This program implements a **fully functional GUI-based calculator** that allows users to input arithmetic expressions via buttons, evaluate them safely, clear inputs, and view results in real time using Tkinter.
