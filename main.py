from sort_algorithms import SortAlgorithms, generate_random_list, time_algorithm

def main():
    sorter = SortAlgorithms()

    # Define test data sizes
    small_data_size = 1000 # 1K Numeric Values
    large_data_size = 10000 # 10K Numeric Values
    extra_large_data_size = 20000 # 20K Numeric Values

    # Generate random data samples
    small_data = generate_random_list(small_data_size)
    large_data = generate_random_list(large_data_size)
    extra_large_data = generate_random_list(extra_large_data_size)

    algorithms = {
        "Bubble Sort": sorter.bubble_sort,
        "Selection Sort": sorter.selection_sort,
        "Insertion Sort": sorter.insertion_sort,
        "Quick Sort": sorter.quick_sort,
        "Merge Sort": sorter.merge_sort,
        "Bucket Sort": sorter.bucket_sort,
        "Heap Sort": sorter.heap_sort,
    }

    # Time results for small data
    small_data_results = []
    for name, algorithm in algorithms.items():
        time_taken = time_algorithm(algorithm, small_data)
        small_data_results.append((name, time_taken))

    # Time results for large data
    large_data_results = []
    for name, algorithm in algorithms.items():
        time_taken = time_algorithm(algorithm, large_data)
        large_data_results.append((name, time_taken))

    # Time results for extra large data
    extra_large_data_results = []
    for name, algorithm in algorithms.items():
        time_taken = time_algorithm(algorithm, extra_large_data)
        extra_large_data_results.append((name, time_taken))
    
    # Sort by execution time (small data)
    small_data_results.sort(key=lambda x: x[1])
    print("Small Data Performance (size={}):".format(small_data_size))
    for idx, (name, time_taken) in enumerate(small_data_results, 1):
        print(f"{idx}) {name}: {time_taken:.5f} seconds")

    # Sort by execution time (large data)
    large_data_results.sort(key=lambda x: x[1])
    print("\nLarge Data Performance (size={}):".format(large_data_size))
    for idx, (name, time_taken) in enumerate(large_data_results, 1):
        print(f"{idx}) {name}: {time_taken:.5f} seconds")

    # Sort by execution time (large data)
    extra_large_data_results.sort(key=lambda x: x[1])
    print("\nExtra Large Data Performance (size={}):".format(extra_large_data_size))
    for idx, (name, time_taken) in enumerate(extra_large_data_results, 1):
        print(f"{idx}) {name}: {time_taken:.5f} seconds")

if __name__ == "__main__":
    main()
   
