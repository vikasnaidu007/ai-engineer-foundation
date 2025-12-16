def load_numbers(file_path):
    """Load a list of numbers from a file."""
    try:
        with open(file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file.readlines()]
        return numbers
    except FileNotFoundError:
        print("File not found.")
        return []
    except ValueError:
        print("File contains non-integer values.")
        return []
def calculate_statistics(numbers):
        if not numbers:
            return {}
        return {
            'mean': sum(numbers) / len(numbers),
            'max': max(numbers),
            'min': min(numbers)
        }
def main():
    file_path = "data/numbers.txt"
    numbers = load_numbers(file_path)
    stats = calculate_statistics(numbers)
    print("Statistics:", stats)


if __name__ == "__main__":
    main()