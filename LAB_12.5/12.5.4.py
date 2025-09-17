import random
import string
import time

# Simulate stock data
def generate_stock_data(n=1000):
    stocks = []
    for _ in range(n):
        symbol = ''.join(random.choices(string.ascii_uppercase, k=4))
        open_price = round(random.uniform(10, 500), 2)
        # Simulate close price with some random change
        close_price = round(open_price * random.uniform(0.95, 1.10), 2)
        stocks.append({
            'symbol': symbol,
            'open': open_price,
            'close': close_price,
            'pct_change': ((close_price - open_price) / open_price) * 100
        })
    return stocks

# Heap Sort implementation for sorting by percentage change
def heapify(arr, n, i, key):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l][key] > arr[largest][key]:
        largest = l
    if r < n and arr[r][key] > arr[largest][key]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)

def heap_sort(arr, key):
    n = len(arr)
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)
    # Extract elements
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, key)
    arr.reverse()  # For descending order

# Search using hash map (dict)
def build_stock_dict(stocks):
    return {stock['symbol']: stock for stock in stocks}

def search_stock(stock_dict, symbol):
    return stock_dict.get(symbol, None)

# Performance comparison
def compare_performance():
    stocks = generate_stock_data(10000)
    stocks_copy = [dict(stock) for stock in stocks]  # For fair comparison

    # Sorting with heap sort
    t0 = time.time()
    heap_sort(stocks, key='pct_change')
    t1 = time.time()
    heap_sort_time = t1 - t0

    # Sorting with built-in sorted()
    t2 = time.time()
    sorted_stocks = sorted(stocks_copy, key=lambda x: x['pct_change'], reverse=True)
    t3 = time.time()
    builtin_sort_time = t3 - t2

    print(f"Heap Sort Time: {heap_sort_time:.6f} seconds")
    print(f"Built-in sorted() Time: {builtin_sort_time:.6f} seconds")

    # Build hash map for searching
    stock_dict = build_stock_dict(stocks)
    # Search for 100 random symbols
    search_symbols = random.sample([s['symbol'] for s in stocks], 100)
    t4 = time.time()
    for sym in search_symbols:
        _ = search_stock(stock_dict, sym)
    t5 = time.time()
    hash_search_time = t5 - t4

    # Search using list (linear search)
    t6 = time.time()
    for sym in search_symbols:
        _ = next((s for s in stocks if s['symbol'] == sym), None)
    t7 = time.time()
    linear_search_time = t7 - t6

    print(f"Hash Map Search Time (100 lookups): {hash_search_time:.6f} seconds")
    print(f"Linear Search Time (100 lookups): {linear_search_time:.6f} seconds")

    print("\nTrade-offs:")
    print("- Heap sort is O(n log n) and efficient for in-place sorting, but Python's built-in sorted() is highly optimized C code and usually faster for most use cases.")
    print("- Hash map (dict) lookups are O(1) on average, much faster than linear search (O(n)).")
    print("- For large datasets, using dict for search and built-in sorted() for sorting is generally optimal in Python.")

# Example usage
if __name__ == "__main__":
    stocks = generate_stock_data(20)
    print("Unsorted Stocks (symbol, open, close, % change):")
    for s in stocks:
        print(f"{s['symbol']}: Open={s['open']}, Close={s['close']}, Change={s['pct_change']:.2f}%")

    # Sort using heap sort
    heap_sort(stocks, key='pct_change')
    print("\nStocks sorted by % change (Heap Sort):")
    for s in stocks:
        print(f"{s['symbol']}: Open={s['open']}, Close={s['close']}, Change={s['pct_change']:.2f}%")

    # Build hash map and search
    stock_dict = build_stock_dict(stocks)
    symbol = stocks[5]['symbol']
    result = search_stock(stock_dict, symbol)
    print(f"\nSearch for symbol '{symbol}': {result}")

    # Compare performance
    print("\n--- Performance Comparison ---")
    compare_performance()
