import pytest
from utils import *


def test_load_data():
    pass


@pytest.mark.parametrize(
    "input_data, expected_result", [
        ("2019-11-13T17:38:04.800051", "13.11.2019"),
        ("2019-12-07T06:17:14.634890", "07.12.2019")
    ]
)
def test_date_format(input_data, expected_result):
    assert date_format(input_data) == expected_result


@pytest.mark.parametrize(
    "input_data, operations_amount, expected_result", [
        ([{
            "id": 482520625,
            "state": "EXECUTED",
            "date": "2019-11-13T17:38:04.800051",
            "operationAmount": {
                "amount": "62814.53",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 38611439522855669794",
            "to": "Счет 46765464282437878125"
        }], 1, [{
            "id": 482520625,
            "state": "EXECUTED",
            "date": "2019-11-13T17:38:04.800051",
            "operationAmount": {
                "amount": "62814.53",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 38611439522855669794",
            "to": "Счет 46765464282437878125"
        }]),
        ([{}], 2, [])
    ]
)
def test_if_executed(input_data, operations_amount, expected_result):
    assert if_executed(input_data, operations_amount) == expected_result


@pytest.mark.parametrize(
    "input_data, expected_result", [
        ("Visa Classic 3414396880443483", "Visa Classic 3414 39** **** 3483"),
        ("Счет 38611439522855669794", "Счет 3861 14** **** **** 9794"),
        ("", "Счет отправителя неизвестен")
    ]
)
def test_sender_format(input_data, expected_result):
    assert sender_format(input_data) == expected_result


@pytest.mark.parametrize(
    "input_data, expected_result", [
        ("Счет 90424923579946435907", "Счет **5907"),
        ("Счет 35158586384610753655", "Счет **3655"),
        ("Счет 43241152692663622869", "Счет **2869"),
        ("Visa Gold 2684274847577419", "Visa Gold **7419"),
    ]
)
def test_receiver_format(input_data, expected_result):
    assert receiver_format(input_data) == expected_result
