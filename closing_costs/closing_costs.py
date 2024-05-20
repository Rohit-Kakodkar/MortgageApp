import pandas as pd

class ClosingCosts(object):
    """
    A class to represent closing costs.
    """
    def __init__(self, escrow, fees, downpayment):
        """
        Initialize the closing costs.

        Args:
            escrow (float): Escrow amounts used towards property payments in the first year.
            fees (float): Fees paid at closing.
            downpayment (float): The down payment.

        """
        self.escrow = escrow
        self.fees = fees
        self.downpayment = downpayment

    def total(self):
        """
        Calculate the total closing costs.

        Returns:
            float: The total closing costs.

        """
        return self.escrow + self.fees + self.downpayment