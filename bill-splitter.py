"""
Day 5 - 2026-10-11
Tool: Bill / Tip Splitter
What it does: Splits a shared bill (with an optional tip or service
charge) equally between any number of people, and shows the tip
amount, the grand total and exactly how much each person pays.
Who it helps: Friends, family or colleagues eating out together,
ordering food in, or sharing any group cost fairly.
"""


def split_bill(total_bill, num_people, tip_percent=0):
    """Return a dict with tip, grand total and per-person amounts.

    All money values are rounded to 2 decimal places. The per-person
    amount is rounded up/down to 2 decimals, so the shares may differ
    from the grand total by a few poisha in total.
    """
    if total_bill < 0:
        raise ValueError("Total bill cannot be negative.")
    if num_people <= 0:
        raise ValueError("Number of people must be at least 1.")
    if tip_percent < 0:
        raise ValueError("Tip percent cannot be negative.")
    tip_amount = round(total_bill * tip_percent / 100, 2)
    grand_total = round(total_bill + tip_amount, 2)
    per_person = round(grand_total / num_people, 2)
    return {
        "tip_amount": tip_amount,
        "grand_total": grand_total,
        "per_person": per_person,
    }


def format_split(total_bill, num_people, tip_percent=0):
    """Return the split as one easy-to-read line."""
    result = split_bill(total_bill, num_people, tip_percent)
    return (
        f"Bill {total_bill:.2f} + tip {result['tip_amount']:.2f} "
        f"= {result['grand_total']:.2f}, split {num_people} ways: "
        f"{result['per_person']:.2f} each"
    )


if __name__ == "__main__":
    # Example 1: four friends at a restaurant, 1850 taka bill, 10% tip
    print(format_split(1850, 4, 10))

    # Example 2: a family lunch with no tip
    print(format_split(2400, 5))

    # Example 3: two people ordering food in, 760 taka, 5% tip
    print(format_split(760, 2, 5))
