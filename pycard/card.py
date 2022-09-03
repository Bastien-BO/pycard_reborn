"""
The class library
"""

from datetime import datetime
from datetime import timedelta

from pycard.data import Brand
from pycard.data import FriendlyBrand
from pycard.data import TESTS_CARDS
from pycard.exceptions import CardNuberNotDigitException
from pycard.exceptions import MaskException


class Card:
    """
    A credit card that may be valid or invalid.
    """

    def __init__(
            self, number: str, month: int, year: int,
            cvc: int = None, holder=None
    ):
        """
        Attaches the provided card data and holder to the card after removing
        non-digits from the provided number.
        """
        if not number.isdigit():
            raise CardNuberNotDigitException(
                f'card number {number} contain non digit character(s)'
            )
        self.cvc: int = cvc
        self.holder: int = holder
        self.month: int = month
        self.number: str = number
        self.year: int = year

    def mask(self) -> str:
        """
        Returns the credit card number with each of the number's digits but the
        first six and the last four digits replaced by an X, formatted the way
        they appear on their respective brands' cards.
        """
        # If the card is invalid, return an "invalid" message
        if not self.is_mod10_valid:
            raise MaskException(
                'Unable to generate card mask, due to mod10 invalid'
            )

        # If the card is an Amex, it will have special formatting
        if self.brand() == Brand.amex.name:
            return f'XXXX-XXXXXX-X{self.number[11:15]}'

        # All other cards
        return f'XXXX-XXXX-XXXX-{self.number[12:16]}'

    def brand(self) -> str:
        """
        # Check if the card is of known type and return it
        """
        # Check if the card is of known type
        for brand in Brand:
            if brand.value.regexp.match(self.number):
                return brand.name

        return 'unknown'

    def friendly_brand(self) -> str:
        """
        Returns the human-friendly brand name of the card.
        """
        for friendly in FriendlyBrand:
            if friendly.name == self.brand():
                return friendly.value
        raise MaskException('Unable to find matching friendly brand')

    def is_test(self) -> bool:
        """
        Returns whether the card's number is a known test number.
        """
        return self.number in TESTS_CARDS

    def is_expired(self) -> bool:
        """
        Returns whether the card is expired.
        """

        today: datetime = datetime.utcnow() - timedelta(hours=11)
        if self.year < today.year or self.month < today.month:
            return True

    def is_valid(self) -> bool:
        """
        Returns whether the card is a valid card for making payments.
        """
        return not self.is_expired and self.is_mod10_valid

    def is_mod10_valid(self) -> bool:
        """
        Returns whether the card's number validates against the mod10
        algorithm (Luhn algorithm), automatically returning False on an empty
        value.
        """

        # Run mod10 on the number
        dub, tot = 0, 0
        for i in range(len(str(self.number)) - 1, -1, -1):
            for c in str((dub + 1) * int(str(self.number)[i])):
                tot += int(c)
            dub = (dub + 1) % 2

        return (tot % 10) == 0
