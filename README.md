# Bill Splitting Calculator

A powerful Python tool to split restaurant bills among friends with customizable options. Calculate tips, assign amounts to named individuals, and save results effortlessly!

This project was built to practice clean Python design, user input validation, and building a practical CLI tool that solves a real-world problem.

---

## Features
Latest change is in **bold**
- Calculates the total bill with tip included
- Supports **even splitting** or **uneven splitting with custom amounts, with the remainder split evenly**
- Tracks amounts owed by **named individuals**
- Optional rounding of per-person amounts (no rounding, 2 decimal places, or rounding up to the nearest dollar)
- **Ensures the final total always matches the bill by adjusting the last person's amount when necessary**
- Saves bill breakdowns to a text file
- Reprompts for invalid input instead of crashing (typo-friendly)
- Gracefully exits on interrupt (`Ctrl+C`) with a clean message
- Allows multiple calculations in a single session
- Clean, formatted output for easy readability

---

## Tech Stack
- Python
- Command-Line Interface (CLI)
- File I/O for saving bill breakdowns
- Input validation and error handling
- Pytest for unit testing

---

## Project Structure
```txt
bill-split-calculator/
├── bill_split.py
├── tests/
│   └── test_bill_split.py
├── .gitignore
└── README.md
```

## How to Run
1. **Prerequisites**: Ensure you have Python 3 installed (`python3 --version` to check).  
2. **Download**: Clone or download this repository to your local machine.  
3. **Run the Script**: Open a terminal in the project folder and execute:

```bash
python3 bill_split.py
```

*(Note: Use `python` instead of `python3` if that’s how Python 3 is configured on your system.)*
   
## Example Usage
Here’s what you’ll see when you run the program:

> === Bill Split Calculator ===<br>
Enter the bill amount (\$): 50<br>
Enter tip percentage (%): 23<br>
Enter number of people to split among: 3<br>
Enter name for person 1: Jacob<br>
Enter name for person 2: Jay<br>
Enter name for person 3: Nick<br>
Even split (e) or uneven split with custom amounts (u)? u<br>
How many people pay a custom amount? (0 to cancel uneven split): 1<br>
Remaining to allocate: \$61.50<br>
Enter name of person 1 paying custom amount: Jay<br>
Enter amount for Jay (\$): 25<br>
> 
> Round the per-person amounts?<br>
1: No rounding (default)<br>
2: Round to nearest cent (2 decimal places)<br>
3: Round up to nearest dollar<br>
Enter choice (1-3): 1<br>
> 
> --- Bill Breakdown ---<br>
Bill Amount: \$50.00<br>
Tip (23.0%): \$11.50<br>
Total (with tip): \$61.50<br>
Jay: \$25.00<br>
Jacob: \$18.25<br>
Nick: \$18.25<br>
> 
> Save breakdown to file? (yes/no): yes<br>
Enter filename (e.g., bill.txt): dominos.txt<br>
Saved to dominos.txt<br>
> 
> Calculate another bill? (yes/no): no<br>
Thanks for using Bill Split Calculator!<br>

And here’s an example where the program handles invalid input gracefully:

> Enter the bill amount (\$): asd<br>
Please enter a valid number.<br>
Enter the bill amount (\$):<br>

---

## Installation
1. Clone the repository:

```bash
git clone https://github.com/JacobDemory/bill-split-calculator.git
```

2. Navigate to the directory:

```bash
cd bill-split-calculator
```

3. Run the script as described above.

---

## Testing
This project includes unit tests for core bill calculation logic such as total calculation, even splits, uneven splits, and rounding behavior.

Install pytest if needed:
```bash
python3 -m pip install pytest
```

Run the test suite:
```bash
python3 -m pytest
```

---

## Future Improvements
- Build a GUI version using Tkinter or a simple web interface
- Add itemized bill support
- Allow editing of previous entries before finalizing the split
- Support multiple currency formats
- Include tax calculation support
- Export breakdowns as CSV

---

## Contributing
Feel free to fork this project, submit pull requests, or open issues for bugs and feature suggestions!  

---

Built with ❤️ by Jacob
