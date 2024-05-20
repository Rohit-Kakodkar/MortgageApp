import pandas as pd
import loan_payments.loan_payments as lp

class Loan(object):
    """
    A class to represent a loan.
    """
    def __init__(self, purchase_price, downpayment, interest_rate_per_year, duration):
        """
        Initialize the loan.

        Args:
            purchase_price (float): The purchase price of the house.
            downpayment (float): The down payment.
            interest_rate_per_year (float): The interest rate per year.
            duration (int): The duration of the loan, in years.

        """
        self.purchase_price = purchase_price
        self.downpayment = downpayment
        self.interest_rate_per_year = interest_rate_per_year
        self.duration = duration

    def monthly_payment(self):
        """
        Calculate the monthly payment for a mortgage.

        Returns:
            float: The monthly payment for the mortgage.

        """
        return lp.monthly_payment(self.purchase_price, self.downpayment, self.interest_rate_per_year, self.duration)

    def amortization_schedule(self, fixed_extra_payment=0):
        """
        Calculate the amortization schedule for a mortgage.

        Returns:
            pandas.DataFrame: The amortization schedule.
        """
        return lp.amortization_schedule(self.purchase_price, self.downpayment, self.interest_rate_per_year, self.duration)
    
    def months_to_20_percent_equity(self, fixed_extra_payment=0):
        """
        Calculate the number of months until the equity reaches 20% of the purchase price.

        Returns:
            int: The number of months until the equity reaches 20% of the purchase price.

        """
        return lp.months_to_20_percent_equity(self.purchase_price, self.downpayment, self.interest_rate_per_year, self.duration, fixed_extra_payment=fixed_extra_payment)
    
    def months_to_pay_off_loan(self, fixed_extra_payment=0):
        """
        Calculate the number of months until the loan is paid off.

        Returns:
            int: The number of months until the loan is paid off.

        """
        return lp.months_to_pay_off(self.purchase_price, self.downpayment, self.interest_rate_per_year, self.duration, fixed_extra_payment=fixed_extra_payment)
    
    def print_loan_info(self):
        """
        Print information about the loan.
        """
        print("Loan info:")
        print("Purchase price: ${:,.2f}".format(self.purchase_price))
        print("Downpayment: ${:,.2f}".format(self.downpayment))
        print("Interest rate per year: {:.2f}%".format(self.interest_rate_per_year * 100))
        print("Duration: {} years".format(self.duration))
    

   