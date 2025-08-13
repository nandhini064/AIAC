def format_name(first, last):
    """
    Formats the full name as "Last, First" with the first letter of each name capitalized.
    Args:
        first (str): First name
        last (str): Last name
    Returns:
        str: Formatted name as "Last, First"
    """
    return f"{last.capitalize()}, {first.capitalize()}"

# Example usage:
if __name__ == "__main__":
    print(format_name("Nandhini", "Rakesh"))  
    print(format_name("Siri", "krupa"))       
    print(format_name("Suma", "Swadha"))      
