import statistics

data = [float(number) for number in open('data.txt').readlines()]
print(f"Mean: {statistics.mean(data)}, Standard Deviation: {statistics.stdev(data)}")
