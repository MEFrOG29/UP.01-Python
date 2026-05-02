numbers = input_data

squared = [x * x for x in numbers]
total = sum(numbers)

output = {
    "squared": squared,
    "sum": total,
    "count": len(numbers)
}