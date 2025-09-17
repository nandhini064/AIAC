import re
from datetime import datetime


def convert_date_format(date_str: str) -> str:
    """Convert date between YYYY-MM-DD and DD-MM-YYYY formats.
    
    Args:
        date_str: Date string in either YYYY-MM-DD or DD-MM-YYYY format
        
    Returns:
        Converted date string in the opposite format
        
    Raises:
        ValueError: If date format is invalid or date doesn't exist
    """
    if not isinstance(date_str, str):
        raise TypeError("Date must be a string")
    
    date_str = date_str.strip()
    
    # Check if input is in YYYY-MM-DD format
    if re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
        try:
            # Parse and validate the date
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            # Convert to DD-MM-YYYY format
            return date_obj.strftime('%d-%m-%Y')
        except ValueError as e:
            raise ValueError(f"Invalid date: {e}")
    
    # Check if input is in DD-MM-YYYY format
    elif re.match(r'^\d{2}-\d{2}-\d{4}$', date_str):
        try:
            # Parse and validate the date
            date_obj = datetime.strptime(date_str, '%d-%m-%Y')
            # Convert to YYYY-MM-DD format
            return date_obj.strftime('%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date: {e}")
    
    else:
        raise ValueError("Date must be in YYYY-MM-DD or DD-MM-YYYY format")


def main():
    """Main function to handle command line input."""
    import sys
    
    if len(sys.argv) == 2:
        # Single argument mode: convert the provided date
        try:
            date_input = sys.argv[1]
            converted = convert_date_format(date_input)
            print(converted)
        except ValueError as e:
            print(f"Error: {e}")
    else:
        # Interactive mode
        print("Date Format Converter")
        print("Converts between YYYY-MM-DD and DD-MM-YYYY formats")
        print("Type 'quit' to exit")
        
        while True:
            try:
                date_input = input("\nEnter date to convert: ").strip()
                
                if date_input.lower() == 'quit':
                    break
                
                if not date_input:
                    print("Please enter a date.")
                    continue
                
                converted = convert_date_format(date_input)
                print(f"Converted: {converted}")
                
            except ValueError as e:
                print(f"Error: {e}")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break


if __name__ == "__main__":
    main()
