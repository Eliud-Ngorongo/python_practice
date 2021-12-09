def sum_numbers(n):
    """prints the number to a certain range,
       tells the current and previous number and the sum of the two"""
    num = 0
    for number in range(10):
        if num == 0:
            print(f"Current number {num} Previous number {num} Sum: {num}")
        else:
            print(f"Current number {number} Previous number {num - 1} Sum: {num + number - 1}")
        num += 1
