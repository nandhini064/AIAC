from typing import Iterable, Tuple
def sum_even_and_odd(numbers: Iterable[int]) -> Tuple[int, int]:
    """Return a tuple of (even_sum, odd_sum) for the given iterable of integers.
    Args:
        numbers: Any iterable of integers (e.g., list, tuple, generator).
    Returns:
        A tuple where the first element is the sum of even numbers and the
        second element is the sum of odd numbers.
    """
    even_sum = 0
    odd_sum = 0
    for value in numbers:
        if value % 2 == 0:
            even_sum += value
        else:
            odd_sum += value
    return even_sum, odd_sum
if __name__ == "__main__":
    raw = input("Enter integers separated by spaces (or commas): ").strip()
    if raw:
        try:
            numbers = [int(x) for x in raw.replace(",", " ").split()]
        except ValueError:
            print("Please enter only integers.")
            raise SystemExit(1)
    else:
        numbers = []
    even_total, odd_total = sum_even_and_odd(numbers)
    print(f"Input: {numbers}")
    print(f"Sum of even numbers: {even_total}")
    print(f"Sum of odd numbers:  {odd_total}")