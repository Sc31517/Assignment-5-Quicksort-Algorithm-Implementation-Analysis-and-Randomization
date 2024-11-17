import random  # To use random functions
import time  # To measure performance
import pandas as pd  # To structure results

# Deterministic Quicksort Implementation
def deterministic_quicksort(array):
    """
    Deterministic Quicksort implementation using the first element as the pivot.
    """
    # Check if the array is trivially sorted
    if len(array) <= 1:
        return array

    # The first element is chosen as the pivot
    pivot = array[0]
    
    # Create partitions around the pivot
    left_partition = [x for x in array[1:] if x <= pivot]
    right_partition = [x for x in array[1:] if x > pivot]
    
    # Recursive call on partitions and merge the results
    return deterministic_quicksort(left_partition) + [pivot] + deterministic_quicksort(right_partition)

# Randomized Quicksort Implementation
def randomized_quicksort(array):
    """
    Randomized Quicksort implementation using a randomly selected pivot.
    """
    # Base case: no sorting needed for one or no element
    if len(array) <= 1:
        return array

    # Select a random pivot from the array
    pivot_index = random.randint(0, len(array) - 1)
    pivot = array[pivot_index]
    
    # Create partitions around the pivot
    less_than_pivot = [x for i, x in enumerate(array) if x <= pivot and i != pivot_index]
    greater_than_pivot = [x for i, x in enumerate(array) if x > pivot]
    
    # Recursively sort the partitions and combine
    return randomized_quicksort(less_than_pivot) + [pivot] + randomized_quicksort(greater_than_pivot)

# Measure Sorting Time
def sort_and_measure(func, array):
    """
    Measures the time taken by the sorting function to execute.
    """
    start_time = time.time()
    func(array)
    end_time = time.time()
    return end_time - start_time

# Generate Different Types of Input Arrays
def generate_input(size, mode):
    """
    Generates arrays of different distributions.
    """
    if mode == "Random":
        return [random.randint(0, 10000) for _ in range(size)]
    elif mode == "Sorted":
        return list(range(size))
    elif mode == "Reverse Sorted":
        return list(range(size, 0, -1))

# Run Tests and Record Performance
def analyze_performance():
    """
    Runs the sorting algorithms on various inputs and records their performance.
    """
    input_sizes = [100, 1000, 5000, 10000]  # Different sizes of inputs
    array_types = ["Random", "Sorted", "Reverse Sorted"]  # Input distributions
    
    performance_data = []  # Store performance results

    for size in input_sizes:
        for mode in array_types:
            # Generate the array
            array = generate_input(size, mode)
            
            # Measure deterministic Quicksort time
            time_deterministic = sort_and_measure(deterministic_quicksort, array.copy())
            
            # Measure randomized Quicksort time
            time_randomized = sort_and_measure(randomized_quicksort, array.copy())
            
            # Record the results
            performance_data.append({
                "Array Size": size,
                "Distribution": mode,
                "Deterministic Time (s)": time_deterministic,
                "Randomized Time (s)": time_randomized
            })
    
    # Convert to a DataFrame for better readability
    df = pd.DataFrame(performance_data)
    return df

# Run the analysis and save results
results = analyze_performance()

# Display the results
print("Performance Comparison of Deterministic and Randomized Quicksort:")
print(results)
