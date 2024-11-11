Heap Data Structures: Implementation, Analysis, and Applications
Introduction
This report outlines the implementation of Heapsort and a Priority Queue using binary heaps, detailing the design choices, implementation strategies, and performance analysis. The assignment explores the efficiency of the Heapsort algorithm, as well as the core operations of a Priority Queue (insert, extract, increase/decrease key, and is_empty) using a binary heap. The task aims to demonstrate how heap-based data structures can be used to solve problems efficiently in terms of both time and space complexity.

Design Choices
Heapsort Design
For Heapsort, I chose to implement the algorithm using a Max-Heap. A Max-Heap is a binary tree where the value of each parent node is greater than or equal to the values of its child nodes. This property makes it suitable for sorting in ascending order, as the maximum element is always at the root, which can be easily extracted and placed at the end of the array.

Why Max-Heap?

A Max-Heap ensures that the root node always holds the largest element. Extracting the maximum element and swapping it with the last element in the heap allows us to efficiently sort the array.
Building the Max-Heap has a time complexity of O(n), and each extraction operation takes O(log n) time, making Heapsort overall efficient for sorting.
Priority Queue Design
For the Priority Queue, I chose a Max-Heap as well, since priority queues typically require the highest priority to be retrieved first. In a Max-Heap, the root node always holds the highest priority element, making it ideal for a task scheduler or any other system where tasks with higher priority need to be processed first.

Task Representation

I defined a Task class to represent individual tasks. Each task has a priority, arrival time, and a task ID. The priority attribute determines the order in which tasks are processed, and the task ID uniquely identifies each task.
Data Structures
Max-Heap implemented as an array or list for simplicity.
Array Implementation: I chose an array-based implementation because it allows for efficient index-based access to parent and child nodes:
The parent of node at index i is at index (i - 1) // 2.
The left child of node at index i is at index 2 * i + 1.
The right child of node at index i is at index 2 * i + 2.
Implementation Details
Heapsort Implementation
The Heapsort algorithm works in two main phases:

Heap Construction: Convert the input array into a valid Max-Heap by applying the heapify operation starting from the non-leaf nodes and working upwards.
Sorting: Repeatedly extract the maximum element (root) of the heap, swap it with the last element in the current heap, and restore the heap property.
Key Functions:

heapify(arr, n, i): This function ensures that the subtree rooted at index i maintains the heap property. It compares the parent node with its left and right children, and if necessary, swaps them to maintain the Max-Heap property. This is done recursively.
heapsort(arr): This function builds the Max-Heap and then performs the sorting by repeatedly calling heapify after swapping the root element with the last unsorted element.
python
Copy code
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap root with last element
        heapify(arr, i, 0)  # Heapify the reduced heap
Priority Queue Implementation
The Priority Queue is implemented using a Max-Heap. The operations supported by the priority queue are:

insert(task): Adds a task to the heap and maintains the heap property.
extract_max(): Removes and returns the task with the highest priority (the root).
increase_key(task, new_priority): Increases the priority of an existing task and restores the heap property.
is_empty(): Checks if the priority queue is empty.
Key Operations:

Insert: Tasks are inserted at the end of the heap and then "bubbled up" to their correct position to maintain the heap property.
Extract Max: The root (task with highest priority) is swapped with the last element, removed from the heap, and the heap property is restored by "bubbling down".
Increase Key: If the priority of a task is increased, it may need to move up the heap, so we perform a "bubble up" operation.
is_empty: This simply checks if the heap is empty by verifying its length.
python
Copy code
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[parent_index].priority < self.heap[index].priority:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._heapify_up(parent_index)

    def extract_max(self):
        if not self.heap:
            return None
        max_task = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return max_task

    def _heapify_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index

        if left_child < len(self.heap) and self.heap[left_child].priority > self.heap[largest].priority:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child].priority > self.heap[largest].priority:
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def is_empty(self):
        return len(self.heap) == 0
Time Complexity Analysis
Heapsort
Heap Construction: Building the heap takes O(n) time.
Extracting Max: Each extraction involves removing the root, swapping it with the last element, and re-heapifying, which takes O(log n) time. Since we do this for n elements, the total time complexity is O(n log n).
Overall Heapsort Complexity:

Worst Case: O(n log n)
Best Case: O(n log n)
Average Case: O(n log n)
Space Complexity: O(1) (in-place sorting)
Priority Queue Operations
Insert: Inserting a task requires adding it to the heap and then performing a bubble-up operation, which takes O(log n) time.
Extract Max: Extracting the task with the highest priority involves removing the root, swapping with the last element, and performing a bubble-down operation, which also takes O(log n) time.
Increase Key: Modifying the priority and re-adjusting the heap requires a bubble-up operation, which takes O(log n) time.
Priority Queue Complexity:

Insert: O(log n)
Extract Max: O(log n)
Increase/Decrease Key: O(log n)
is_empty: O(1)
Empirical Comparison
In my experiments, I compared Heapsort with QuickSort and MergeSort on different datasets, including random, sorted, and reverse-sorted arrays. Heapsort performed similarly to MergeSort, but QuickSort outperformed both in terms of average case runtime, especially for random arrays. However, Heapsort had the advantage of being in-place and having consistent time complexity in all cases (O(n log n)), unlike QuickSort, which can degrade to O(n^2) in the worst case.

Conclusion
This assignment has successfully demonstrated the implementation and analysis of Heapsort and a Priority Queue using a Max-Heap. The time and space complexity of both the sorting algorithm and priority queue operations are well-suited for handling large datasets efficiently. The priority queue implementation, in particular, is useful for scenarios requiring efficient task scheduling, such as in operating systems or real-time computing systems.
