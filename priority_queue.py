class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

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

if __name__ == "__main__":
    pq = PriorityQueue()
    task1 = Task(1, 10, 1, 5)
    task2 = Task(2, 5, 2, 6)
    pq.insert(task1)
    pq.insert(task2)
    print(pq.extract_max().task_id) 

