## Create a function to calculate the monthly payment for my mortgate
import pandas as pd

def monthly_payment(purchase_price, downpayment, interest_rate_per_year, duration):
    """
    Calculate the monthly payment for a mortgage.

    Args:
        purchase_price (float): The purchase price of the house.
        downpayment (float): The down payment.
        interest_rate_per_year (float): The interest rate per year.
        duration (int): The duration of the loan, in years.

    Returns:
        float: The monthly payment for the mortgage.

    """

    # Calculate the principal.
    principal = purchase_price - downpayment

    # Calculate the monthly interest rate.
    interest_rate_per_month = interest_rate_per_year / 12.0

    # Calculate the duration in months.
    duration_months = duration * 12

    # Calculate the monthly payment.
    payment = (principal * interest_rate_per_month) / (1 - (1 + interest_rate_per_month) ** (-duration_months))

    return payment

## define my amortization schedule

def amortization_schedule(purchase_price, downpayment, interest_rate_per_year, duration):
    """
    Calculate the amortization schedule for a mortgage.

    Args:
        purchase_price (float): The purchase price of the house.
        downpayment (float): The down payment.
        interest_rate_per_year (float): The interest rate per year.
        duration (int): The duration of the loan, in years.

    Returns:
        pandas.DataFrame: The amortization schedule.
    """

    # Calculate the principal.
    principal = purchase_price - downpayment

    # Calculate the monthly payment.
    payment = monthly_payment(purchase_price, downpayment, interest_rate_per_year, duration)

    # Initialize the variables to build the amortization schedule.
    index = range(1, duration * 12 + 1)
    current_month = 1
    current_principal = principal
    interest_paid = 0
    principal_paid = 0

    # Create an empty list to store the data.
    data = []

    # Loop through the duration of the loan to create the amortization schedule.
    while current_month <= duration * 12:

        # Calculate the interest paid.
        interest_paid = current_principal * (interest_rate_per_year / 12)

        # Calculate the principal paid.
        principal_paid = payment - interest_paid

        # Calculate the new principal.
        new_principal = current_principal - principal_paid

        # Store the values in the data list.
        data.append((current_month, current_principal, interest_paid, principal_paid, new_principal))

        # Update the variables for the next loop iteration.
        current_month += 1
        current_principal = new_principal

    # Create a DataFrame from the data list.
    df = pd.DataFrame(data, columns=["Month", "Starting_Principal", "Interest", "Principal", "Ending_Principal"])

    return df

## calculate how long will it take to pay off my mortgage

def months_to_pay_off(purchase_price, downpayment, interest_rate_per_year, duration, fixed_extra_payment=0):
    """
    Calculate the number of months required to pay off a mortgage.

    Args:
        purchase_price (float): The purchase price of the house.
        downpayment (float): The down payment.
        interest_rate_per_year (float): The interest rate per year.
        duration (int): The duration of the loan, in years.
        fixed_extra_payment (float): Fixed extra payment to be made each month.

    Returns:
        int: The number of months required to pay off the mortgage.
    """
    # Calculate the principal.
    principal = purchase_price - downpayment

    # Calculate the monthly payment.
    payment = monthly_payment(purchase_price, downpayment, interest_rate_per_year, duration)

    # Initialize the variables to build the amortization schedule.
    current_month = 1
    current_principal = principal
    interest_paid = 0
    principal_paid = 0

    # Loop through the duration of the loan to create the amortization schedule.
    while current_month <= duration * 12:

        # Calculate the interest paid.
        interest_paid = current_principal * (interest_rate_per_year / 12)

        # Calculate the principal paid.
        principal_paid = payment - interest_paid + fixed_extra_payment

        # Calculate the new principal.
        new_principal = current_principal - principal_paid

        # Check if the loan has been paid off.
        if new_principal <= 0:
            break

        # Update the variables for the next loop iteration.
        current_month += 1
        current_principal = new_principal

    return current_month

## calculate how much will it take to get to 20% equity

def months_to_20_percent_equity(purchase_price, down_payment, interest_rate_per_year, duration, fixed_extra_payment=0):
    """
    Calculate the number of months required to get to 20% equity.

    Args:
        purchase_price (float): The purchase price of the house.
        down_payment (float): The down payment.
        interest_rate_per_year (float): The interest rate per year.
        duration (int): The duration of the loan, in years.
        fixed_extra_payment (float): Fixed extra payment to be made each month.

    Returns:
        int: The number of months required to get to 20% equity.
    """

    # Calculate the principal.
    principal = purchase_price - down_payment

    # Calculate the monthly payment.
    payment = monthly_payment(purchase_price, down_payment, interest_rate_per_year, duration)

    # Initialize the variables to build the amortization schedule.
    current_month = 1
    current_principal = principal
    interest_paid = 0
    principal_paid = 0
    equity = down_payment

    # Loop through the duration of the loan to create the amortization schedule.
    while current_month <= duration * 12:

        # Calculate the interest paid.
        interest_paid = current_principal * (interest_rate_per_year / 12)

        # Calculate the principal paid.
        principal_paid = payment - interest_paid + fixed_extra_payment

        # Calculate the new principal.
        new_principal = current_principal - principal_paid

        # Calculate the equity.
        equity += principal_paid

        # Check if the equity is greater than or equal to 20% of the purchase price.
        if equity >= 0.2 * purchase_price:
            break

        # Update the variables for the next loop iteration.
        current_month += 1
        current_principal = new_principal

    return current_month