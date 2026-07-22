import math
import sys


def get_float_input(prompt, min_value=None, max_value=None):
    """Prompt the user for a valid floating-point number."""
    while True:
        try:
            value = float(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Please enter a value of at least {min_value}.")
                continue

            if max_value is not None and value > max_value:
                print(f"Please enter a value no more than {max_value:.2f}.")
                continue

            return value
        except ValueError:
            print("Please enter a valid number.")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting calculator...")
            sys.exit(0)


def get_int_input(prompt, min_value=None, max_value=None):
    """Prompt the user for a valid integer."""
    while True:
        try:
            value = int(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Please enter a value of at least {min_value}.")
                continue

            if max_value is not None and value > max_value:
                print(f"Please enter a value no more than {max_value}.")
                continue

            return value
        except ValueError:
            print("Please enter a valid integer.")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting calculator...")
            sys.exit(0)


def calculate_total(bill_amount, tip_percent):
    """Return the total bill amount including tip."""
    tip_amount = bill_amount * (tip_percent / 100)
    total = bill_amount + tip_amount
    return tip_amount, total


def split_evenly(people, total):
    """Split the total evenly among all people."""
    amount = total / len(people)
    return [(person, amount, "") for person in people]


def split_with_custom_amounts(people, total, custom_amounts):
    """Apply custom amounts first, then split the remainder evenly."""
    breakdown = []
    remaining = total

    for person, amount in custom_amounts.items():
        breakdown.append((person, amount, ""))
        remaining -= amount

    remaining_people = [person for person in people if person not in custom_amounts]

    if remaining_people:
        amount_per_person = remaining / len(remaining_people)
        for person in remaining_people:
            breakdown.append((person, amount_per_person, ""))

    return breakdown


def apply_rounding(breakdown, total, round_up=False):
    """Round each person's amount while keeping the final total accurate."""
    rounded_breakdown = []
    running_total = 0.0

    for index, (name, amount, _) in enumerate(breakdown):
        is_last_person = index == len(breakdown) - 1

        if not is_last_person:
            if round_up:
                remaining_available = max(0, round(total - running_total, 2))
                rounded_amount = min(math.ceil(amount), remaining_available)
                note = " (rounded up to nearest dollar)"
            else:
                rounded_amount = round(amount, 2)
                note = ""

            rounded_breakdown.append((name, rounded_amount, note))
            running_total += rounded_amount
        else:
            if round_up:
                rounded_amount = round(total - running_total, 2)
                note = " (adjusted to match total)"
            else:
                rounded_amount = round(total - running_total, 2)
                expected_amount = round(amount, 2)
                note = " (adjusted to match total)" if abs(rounded_amount - expected_amount) > 0.01 else ""

            rounded_breakdown.append((name, rounded_amount, note))

    return rounded_breakdown


def print_breakdown(bill_amount, tip_percent, tip_amount, total, breakdown):
    """Print a formatted bill breakdown."""
    print("\n--- Bill Breakdown ---")
    print(f"Bill Amount: ${bill_amount:.2f}")
    print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
    print(f"Total (with tip): ${total:.2f}")

    for name, amount, note in breakdown:
        print(f"{name}: ${amount:.2f}{note}")


def save_breakdown(filename, bill_amount, tip_percent, tip_amount, total, breakdown):
    """Save the bill breakdown to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Bill Breakdown\n")
        file.write(f"Bill Amount: ${bill_amount:.2f}\n")
        file.write(f"Tip ({tip_percent}%): ${tip_amount:.2f}\n")
        file.write(f"Total (with tip): ${total:.2f}\n")

        for name, amount, note in breakdown:
            file.write(f"{name}: ${amount:.2f}{note}\n")


def collect_people(num_people):
    """Collect unique names for everyone included in the bill split."""
    people = []

    for index in range(num_people):
        while True:
            try:
                name = input(f"Enter name for person {index + 1}: ").strip()

                if not name:
                    print("Name cannot be empty.")
                elif name in people:
                    print("Name must be unique.")
                else:
                    people.append(name)
                    break
            except (KeyboardInterrupt, EOFError):
                print("\nExiting calculator...")
                sys.exit(0)

    return people


def collect_custom_amounts(people, total):
    """Collect custom payment amounts for uneven bill splitting."""
    custom_amounts = {}
    remaining = total

    max_custom_people = len(people) - 1
    num_custom = get_int_input(
        "How many people pay a custom amount? (0 to cancel uneven split): ",
        min_value=0,
        max_value=max_custom_people,
    )

    if num_custom == 0:
        return None

    for index in range(num_custom):
        print(f"Remaining to allocate: ${remaining:.2f}")

        while True:
            try:
                name = input(f"Enter name of person {index + 1} paying custom amount: ").strip()

                if name not in people:
                    print(f"{name} is not in the group. Choose from: {', '.join(people)}")
                elif name in custom_amounts:
                    print(f"{name} already has a custom amount.")
                else:
                    break
            except (KeyboardInterrupt, EOFError):
                print("\nExiting calculator...")
                sys.exit(0)

        amount = get_float_input(f"Enter amount for {name} ($): ", min_value=0, max_value=remaining)
        custom_amounts[name] = amount
        remaining -= amount

    return custom_amounts


def ask_yes_no(prompt):
    """Ask a yes/no question and return True for yes."""
    while True:
        try:
            answer = input(prompt).lower().strip()

            if answer in ["yes", "y"]:
                return True
            if answer in ["no", "n"]:
                return False

            print("Please enter yes or no.")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting calculator...")
            sys.exit(0)


def calculate_bill_split():
    """Run one bill split calculation."""
    print("=== Bill Split Calculator ===")

    bill_amount = get_float_input("Enter the bill amount ($): ", min_value=0)
    tip_percent = get_float_input("Enter tip percentage (%): ", min_value=0)
    num_people = get_int_input("Enter number of people to split among: ", min_value=1)

    tip_amount, total = calculate_total(bill_amount, tip_percent)
    people = collect_people(num_people)

    while True:
        split_type = input("Even split (e) or uneven split with custom amounts (u)? ").lower().strip()

        if split_type in ["e", "u"]:
            break

        print("Please enter 'e' or 'u'.")

    if split_type == "u":
        custom_amounts = collect_custom_amounts(people, total)
        if custom_amounts:
            breakdown = split_with_custom_amounts(people, total, custom_amounts)
        else:
            breakdown = split_evenly(people, total)
    else:
        breakdown = split_evenly(people, total)

    print("\nRound the per-person amounts?")
    print("1: No rounding")
    print("2: Round up to nearest dollar")
    rounding_choice = input("Enter choice (1-2): ").strip()

    round_up = rounding_choice == "2"
    final_breakdown = apply_rounding(breakdown, total, round_up)

    print_breakdown(bill_amount, tip_percent, tip_amount, total, final_breakdown)

    if ask_yes_no("\nSave breakdown to file? (yes/no): "):
        filename = input("Enter filename, such as bill.txt: ").strip()
        save_breakdown(filename, bill_amount, tip_percent, tip_amount, total, final_breakdown)
        print(f"Saved to {filename}")


def main():
    """Run the calculator until the user chooses to stop."""
    while True:
        calculate_bill_split()

        if not ask_yes_no("\nCalculate another bill? (yes/no): "):
            print("Thanks for using Bill Split Calculator!")
            break


if __name__ == "__main__":
    main()
