import sys
def calculate_interest(invest=100, rate=0.03, year=2):
    total = invest + invest * rate
    for x in range(0, year):
        total += total * rate
    return total

print(sys.stdin.readline()) 

print(calculate_interest(100, 0.03, 5))

