from dataclasses import dataclass

_average_rate = {
    "CHF": {
        "CHF": 1,
        "USD": 0.91,
        "UAH": 0.023,
    },
    "USD": {
        "CHF": 1.09,
        "UAH": 42,
    },
    "UAH": {
        "CHF": 43.48,
        "USD": 42,
    },
}

MIDDLE_CURRENCY = "CHF"


def convert(value: float, currency_from: str, currency_to: str) -> float:
    if currency_from == currency_to:
        return value

    if currency_to == MIDDLE_CURRENCY:
        coefficient = 1 / _average_rate[currency_from][MIDDLE_CURRENCY]
    else:
        coefficient = (
            _average_rate[currency_to][MIDDLE_CURRENCY]
            / _average_rate[currency_from][MIDDLE_CURRENCY]
        )
    return value * coefficient


@dataclass
class Price:
    value: float
    currency: str

    def __add__(self, other: "Price") -> "Price":
        return self.add_prices(other)

    def add_prices(self, other: "Price") -> "Price":
        if self.currency == other.currency:
            return Price(value=self.value + other.value, currency=self.currency)

        left_in_middle: float = convert(
            value=self.value,
            currency_from=self.currency,
            currency_to=MIDDLE_CURRENCY,
        )
        right_in_middle: float = convert(
            value=other.value,
            currency_from=other.currency,
            currency_to=MIDDLE_CURRENCY,
        )
        total_in_left_currency: float = convert(
            value=left_in_middle + right_in_middle,
            currency_from=MIDDLE_CURRENCY,
            currency_to=self.currency,
        )
        return Price(value=total_in_left_currency, currency=self.currency)


hotel_price = float(input("Enter hotel price: "))
hotel_currency = input("Enter hotel currency: ")

flight_price = float(input("Enter the flight price: "))
flight_currency = input("Enter your flight currency: ")

flight = Price(value=flight_price, currency=flight_currency)
hotel = Price(value=hotel_price, currency=hotel_currency)

total: Price = flight.add_prices(hotel)
print(total)
