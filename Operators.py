m = float(input())
tip = int(input())
tax = int(input())
TC = m + (m * (tip/100)) + (m * (tax/100))
print('The total meal cost is', round(TC), 'dollars.')