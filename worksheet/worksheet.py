import pandas as pd
import loan_payments.loan_payments as lp
import closing_costs.closing_costs as closing_costs
import loan.loan as loan

class Worksheet(object):
    """
    A class to represent a loan worksheet.
    """
    def __init__(self, purchase_price, downpayment, interest_rate_per_year, duration, escrow, fees, additional_payments, mortgate_insurance=0, total_monthly_payment=0):
        """
        Initialize the loan worksheet.

        Args:
            purchase_price (float): The purchase price of the house.
            downpayment (float): The down payment.
            interest_rate_per_year (float): The interest rate per year.
            duration (int): The duration of the loan, in years.
            escrow (float): Escrow amounts used towards property payments in the first year.
            fees (float): Fees paid at closing.
            additional_payments (float): Additional payments made each month (Real estate taxes etc).

        """
        self.loan = loan.Loan(purchase_price, downpayment, interest_rate_per_year, duration)
        self.closing_costs = closing_costs.ClosingCosts(escrow, fees, downpayment)
        self.additional_payments = additional_payments
        self.mortgate_insurance = mortgate_insurance
        if total_monthly_payment == 0:
            self.total_monthly_payment = self.loan.monthly_payment() + self.additional_payments + self.mortgate_insurance
        else:
            self.total_monthly_payment = total_monthly_payment

        self.fixed_extra_payment = self.total_monthly_payment - self.loan.monthly_payment() - self.additional_payments - self.mortgate_insurance
        self.monthly_payment = self.loan.monthly_payment() + self.additional_payments + self.mortgate_insurance
        self.months_to_20_percent_equity = self.loan.months_to_20_percent_equity(fixed_extra_payment=self.fixed_extra_payment)
        self.total_mortgage_insurance_payments = self.mortgate_insurance * self.months_to_20_percent_equity
        self.months_to_pay_off_loan = self.loan.months_to_pay_off_loan(fixed_extra_payment=self.fixed_extra_payment)

    def print_worksheet(self):
        """
        Print the loan worksheet.

        """
        print("Loan Worksheet")
        print("--------------")
        print("Monthly Payment: {:.2f}".format(self.monthly_payment))
        print("Extra Payment: {:.2f}".format(self.fixed_extra_payment))
        print("Closing Costs: {:.2f}".format(self.closing_costs.total()))
        print("Total Mortgage Insurance: {:.2f}".format(self.total_mortgage_insurance_payments))
        print("Years to 20% equity: {:.2f}".format(self.months_to_20_percent_equity/12))
        print("Years to Pay Off Loan: {:.2f}".format(self.months_to_pay_off_loan/12))

    def get_monthly_payment(self):
        """
        Calculate the monthly payment for the mortgage.

        Returns:
            float: The monthly payment for the mortgage.

        """
        return self.total_monthly_payment
    
    def total_mortgage_insurance(self):
        """
        Calculate the total mortgage insurance payments.

        Returns:
            float: The total mortgage insurance payments.

        """
        return self.total_mortgage_insurance_payments
    
    def total_costs(self):
        """
        Calculate the total closing costs.

        Returns:
            float: The total closing costs.

        """
        return self.closing_costs.total() + self.total_mortgage_insurance_payments
    
    def book_monthly_payment(self):
        """
        Calculate the monthly payment for the mortgage.

        Returns:
            float: The monthly payment for the mortgage.

        """
        return self.monthly_payment

## compare 2 worksheets - monthly payments, total closing costs, total mortgage insurance payments, months to break even
def compare_worksheets(worksheet_1, worksheet_2):
    """
    Compare two worksheets.

    Args:
        worksheet_1 (Worksheet): The first worksheet.
        worksheet_2 (Worksheet): The second worksheet.

    Returns:
        pandas.DataFrame: A dataframe with the comparison results.

    """
    extra_costs = worksheet_1.total_costs() - worksheet_2.total_costs()
    extra_monthly_payment = worksheet_1.book_monthly_payment() - worksheet_2.book_monthly_payment()
    if extra_costs < 0 and extra_monthly_payment < 0:
        print("Worksheet 1 is better than Worksheet 2")
    elif extra_costs > 0 and extra_monthly_payment > 0:
        print("Worksheet 2 is better than Worksheet 1")
    else:
        months_to_break_even = abs(extra_costs / extra_monthly_payment)
        if extra_costs < 0:
            print("Worksheet 1 is better if you refinance within {:.2f} years".format(months_to_break_even/12)) 
        else:
            print("Worksheet 2 is better if you refinance within {:.2f} year".format(months_to_break_even/12))

    data = {
        "Worksheet 1": [
            worksheet_1.get_monthly_payment(),
            worksheet_1.book_monthly_payment(),
            worksheet_1.total_costs(),
            worksheet_1.closing_costs.total(),
            worksheet_1.total_mortgage_insurance_payments,
            worksheet_1.months_to_20_percent_equity,
        ],
        "Worksheet 2": [
            worksheet_2.get_monthly_payment(),
            worksheet_2.book_monthly_payment(),
            worksheet_2.total_costs(),
            worksheet_2.closing_costs.total(),
            worksheet_2.total_mortgage_insurance_payments,
            worksheet_2.months_to_20_percent_equity,
        ]
    }
    return pd.DataFrame(data, index=["Monthly Payment", "Book Monthly Payment", "Total Costs", "Closing Costs", "Mortgage Insurance", "Months to Pay Off Mortgage Insurance"])




