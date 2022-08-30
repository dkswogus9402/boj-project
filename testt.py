class CNode: 
    def __init__(self, item, prev = None, next = None):
        self.item = item
        self.prev = prev
        self.next = next

class CList:
    def __init__(self):
        self.head = None

    def insert_front(self, item):
        Node = CNode(item)
        first = self.head

        if first == None:
            Node.next = Node
            Node.prev = Node
            self.head = Node
            return
        
        last = self.head.prev

        last.next = Node
        Node.next = first
        first.prev = Node
        Node.prev = last
        self.head = Node

    def print_head(self):
        if self.head == None:
            print("비어있습니다")
            return
        
        p = self.head

        while p:
            if p.next != self.head:
                print(p.item,"<-> ",end="")
            else:
                print(p.item)
            
            p = p.next
            if p == self.head:
                break
        
    def delete_front(self):
        target = self.head
        if target == None:
            return None
        
        if target.next == target:
            self.head = None
        else:
            self.head = target.next
            target.next.prev = target.prev
            target.prev.next = target.next
        return target

    def delete_back(self):
        p = self.head

        if p == None:
            print("비어있습니다")
            return
        
        if p == p.next:
            target = self.head
            self.head = None
            return target
            
        target = p.prev
        t_next = target.next
        t_prev = target.prev

        t_prev.next = t_next
        t_next.prev = t_prev
        return target
    
    def delete_target(self, target):
        p = self.head

        if p == None:
            return

        if p == p.next:
            self.head = None
            return
        
        while p:
            if p.item[1] == target:
                t_next = p.next
                t_prev = p.prev

                t_prev.next = t_next
                t_next.prev = t_prev
                break

            p = p.next

            if p == self.head:
                print("찾지 못했습니다.")
                break
        return

    def search_target(self, target):  
        if self.head == None:
            #print("리스트가 비어있습니다.")
            return False
        
        p = self.head
        index = 1
        while p:            

            if p.item[1] == target:
                return p
            index += 1
            p = p.next
            
            if p == self.head:
                break
        return False  


class Q:
    def __init__(self):
        self.queue = CList()
        self.count = 0
    
    def enqueue(self, item):
        self.queue.insert_front(item)
        self.count += 1
        return
    
    def dequeue(self):
        if (self.count > 0):
            self.count -= 1
            cnode = self.queue.delete_back()
            return cnode.item
        return None
    
    def dequeue_target(self, target):
        if (self.count > 0):
            self.count -= 1
            cnode = self.queue.search_target(target)
            self.queue.delete_target(target)
            return cnode.item
        return None

    def size(self):
        return self.count
    
    def print_queue(self):
        self.queue.print_head()


test_queue = Q()
test_queue.enqueue(("qwe",1))

test_queue.print_queue()
a = test_queue.dequeue_target(1)
test_queue.print_queue()
print(a)