# Assignment-4
Assignment 4: Heap Data Structures - Implementation, Analysis, and Applications
Overview
In this homework assignment, I am working with heaps and some of their applications. So far, Heapsort has been concerned with sorting and priority queues with task management. The goal is to implement and analyze the Heapsort algorithm, compare its running times with those of other algorithms like Quicksort and Merge Sort, and then implement a priority queue with a binary heap.

Key Components of the Assignment:
Heapsort Implementation:
I implemented the Heapsort algorithm using a max-heap to sort an array of numbers.
Heapsort is known for its O(n log n) time complexity in all cases, whether the input is already sorted, random, or reverse-sorted.
Priority Queue:
I implemented a priority queue using a binary heap data structure.
The queue supports operations like inserting tasks, extracting the task with the highest priority, and adjusting the priority of tasks.
This implementation is useful for managing tasks with dynamic priorities in real-world applications like scheduling.
Project Structure
heapsort.py: The Python implementation of the Heapsort algorithm.
priority_queue.py: The Python implementation of the priority queue using a binary heap.
report.md: A report where I detail the design decisions, analyze time complexities, and discuss performance comparisons with other algorithms.
README.md: This file, providing an overview of the assignment, instructions on how to run the code, and a summary of the results.
How to Run the Code
Prerequisites
Ensure you have Python 3.x installed on your system. If not, download it from the official website: Python Downloads.
Running Heapsort
Open a terminal or command prompt.
Navigate to the project directory where heapsort.py is located.
Run the following command:
bash
Copy code
python heapsort.py
This will execute the Heapsort algorithm on an example array and print the sorted array to the console. You can modify the array inside the script to test different inputs.
Running the Priority Queue
Open a terminal or command prompt.
Navigate to the project directory where priority_queue.py is located.
Run the following command:
bash
Copy code
python priority_queue.py
This will run the Priority Queue operations. You can see how tasks are inserted, extracted, and have their priorities modified. Feel free to modify the priority_queue.py file to test with different tasks and priorities.
Example Usage
Here’s an example of how you might use Heapsort and the Priority Queue:
Heapsort:
python
Copy code
# Example usage of Heapsort
arr = [4, 10, 3, 5, 1]
heapsort(arr)
print("Sorted array:", arr)
Priority Queue:
python
Copy code
# Example usage of the Priority Queue
pq = PriorityQueue()
pq.insert(Task(1, 3, "2024-11-01", "2024-11-02"))
pq.insert(Task(2, 1, "2024-11-02", "2024-11-03"))
pq.extract_max()
Summary of Findings
Heapsort Algorithm:
Time Complexity: The time complexity of Heapsort is O(n log n) in all cases: worst, best, and average. This is because building the heap takes O(n) time, and then performing n extractions, each taking O(log n) time. So, it’s efficient and predictable.
Comparison with Other Sorting Algorithms:
Quicksort: Whereas Quicksort has an average time complexity of O(n log n) that degrades to O(n^2) in the worst case, Heapsort always guarantees O(n log n) bounds and hence can be more reliable sometimes.
Merge Sort: Merge Sort also runs in O(n log n) time but requires O(n) extra space for the merging process, while Heapsort is an in-place sort, meaning it doesn’t require extra space.
Priority Queue:
Operations:
Insert: Insert a new task into the heap. Time complexity is O(log n).
Extract Max: Extract the highest-priority task. Time complexity is O(log n).
Increase/Decrease Key: Modify the priority of an existing task and maintain the heap property. Time complexity is O(log n).
is_empty: Checks if the queue is empty.
Real-World Applications: Priority queues are widely used in systems like task schedulers (e.g., CPU scheduling), bandwidth management, and resource allocation, where we need to process tasks in order of priority rather than arrival time.
Conclusion
With this assignment, I had the opportunity to delve deeper into heap data structures, which play an important role both in sorting algorithms, such as Heapsort, and in constructing efficient priority queues. Implementing these structures, including their performance analysis and a comparison of results with Quicksort and Merge Sort algorithms, helped me learn how to make judgments regarding the efficiency of algorithms in different contexts. TheThe priority queue implementation also gave me insight into how dynamic priority management works in real-world systems.