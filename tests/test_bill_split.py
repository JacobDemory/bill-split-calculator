from bill_split import (
    apply_rounding,
    calculate_total,
    split_evenly,
    split_with_custom_amounts,
)


def test_calculate_total():
    tip, total = calculate_total(50, 20)

    assert tip == 10
    assert total == 60


def test_split_evenly():
    people = ["Jacob", "Jay", "Nick"]
    result = split_evenly(people, 60)

    assert len(result) == 3
    assert result[0][1] == 20
    assert result[1][1] == 20
    assert result[2][1] == 20


def test_split_with_custom_amounts():
    people = ["Jacob", "Jay", "Nick"]
    custom_amounts = {"Jay": 25}

    result = split_with_custom_amounts(people, 61.50, custom_amounts)
    amounts = {name: amount for name, amount, _ in result}

    assert amounts["Jay"] == 25
    assert amounts["Jacob"] == 18.25
    assert amounts["Nick"] == 18.25


def test_apply_rounding_keeps_total_accurate():
    breakdown = [
        ("Jacob", 10.333, ""),
        ("Jay", 10.333, ""),
        ("Nick", 10.334, ""),
    ]

    result = apply_rounding(breakdown, 31, round_up=False)
    total = sum(amount for _, amount, _ in result)

    assert total == 31