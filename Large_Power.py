def large_power(base, exponent):
    # Calculate base raised to the exponent
    result = base ** exponent
    
    # Test if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False
