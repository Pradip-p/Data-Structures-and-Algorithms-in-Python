# Queue follows FIFO
# Enqueue: Add an element to the end of the queue
# Dequeue: Remove an element from the front of the queue
# check_Empty: Check if the queue is empty


class Queue:
    
    def __init__(self):
        self.queue = []
        
    def disply(self):
        print(self.queue)
        
    def check_Empty(self):
        return len(self.queue)
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.check_Empty() == 0:
            print("Empty Queue")
        else:
            self.queue.pop(0)
    
    
queue = Queue()
queue.enqueue(10)
queue.enqueue(10)
queue.enqueue(10)
queue.enqueue(10)
queue.enqueue(10)
queue.dequeue()
queue.disply()

# Time Complexity => O(n)
