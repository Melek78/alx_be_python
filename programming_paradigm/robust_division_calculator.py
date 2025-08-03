def safe_divide(numerator, denominator):
    try:
         numerator = float(numerator)
         denominator = float(denominator)
         if denominator == 0:
             raise ZeroDivisionError("Cannot divide by zero.")
         result = numerator / denominator
         return(f"The result is {result}")
    except ValueError:
        return("Error: Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        return("Error: Cannot divide by zero.")