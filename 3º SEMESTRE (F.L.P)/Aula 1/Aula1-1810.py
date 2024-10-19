# Objetos vazios
# >>> o = object()
# >>> o.x = 5
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: 'object' object has no attribute 'x'

def calculate_percentage_change(lowest, highest):
    if lowest > highest:
        lowest, highest = highest, lowest
    return highest / lowest - 1
 
def get_stock_with_highest_percentage_change(stock1, stock2):
    code1, _, lowest_price1, highest_price1 = stock1
    code2, _, lowest_price2, highest_price2 = stock2
 
    percentage_change1 = calculate_percentage_change(lowest_price1, highest_price1)
    percentage_change2 = calculate_percentage_change(lowest_price2, highest_price2)
 
    if percentage_change1 > percentage_change2:
        return code1, percentage_change1
    else:
        return code2, percentage_change2
 
stock = ("GOOGL", 1200.0, 1100.0, 1300.0)
 
result = get_stock_with_highest_percentage_change(
    ("AAPL", 150.0, 140.0, 160.0), 
    stock
)
 
print(f"Stock with the highest percentage change: {result[0]}")
print(f"Average value of the share with the highest percentage change: {result[1]}")
