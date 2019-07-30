import statistics

data = [float(number) for number in open('data.txt').readlines()]
mean = statistics.mean(data)
standard_deviation = statistics.stdev(data)

print(f"Mean: {mean}, Standard Deviation: {standard_deviation}")
