from typing import Union
Number = Union[int, float]
def grade_from_score(score: Number) -> str:
    """Return letter grade for a numeric score using standard ranges.
    Ranges:
      90-100 -> A
      80-89  -> B
      70-79  -> C
      60-69  -> D
      <60    -> F
    """
    if not isinstance(score, (int, float)):
        raise TypeError("score must be a number")
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100 inclusive")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"
def _cli() -> None:
    import sys
    if len(sys.argv) == 2:
        try:
            value = float(sys.argv[1])
        except ValueError:
            print("Invalid number.")
            return
        try:
            print(grade_from_score(value))
        except (TypeError, ValueError) as exc:
            print(str(exc))
        return
    try:
        raw = input("Enter marks (0-100): ").strip()
        value = float(raw)
    except Exception:
        print("Invalid input.")
        return
    try:
        print(grade_from_score(value))
    except (TypeError, ValueError) as exc:
        print(str(exc))
if __name__ == "__main__":
    _cli()


