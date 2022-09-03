"""
All library exceptions
"""


class PycardRebornException(BaseException):
    """
    Global pycard reborn library error
    """
    pass


class CardNumberException(PycardRebornException):
    """
    All errors related to card number
    """
    pass


class CardNuberNotOnlyDigitException(CardNumberException):
    """
    Card number do not contain only digits
    """


class MaskException(PycardRebornException):
    """
    Unable to create a valid card mask
    """
    pass
