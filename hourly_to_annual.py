def hourly(x):
    """enter hourly salary and return annual salary"""
    ann_salary = x * 40.0 * 52.0 #assumes 40 hours a week and 52 weeks in a year
    print(f"The anual salary is ${ann_salary:,.2f}")

x = float(input("Enter the hourly salary in dollars.  "))

hourly(x)
