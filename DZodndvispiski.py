class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

#добавление в произвольное место
    def InsertNth(self,i,x):
        if self.first == None:
            self.last = self.first = Node(x, None)
            return
        if i == 0:
          self.first = Node(x,self.first)
          return
        curr=self.first
        count = 0
        while curr != None:
            count+=1
            if count == i:
              curr.next = Node(x,curr.next)
              if curr.next.next == None:
                self.last = curr.next
              break
            curr = curr.next
        return

#удаление элемента
    def Del(self,i):
        if (self.first == None):
          return
        curr = self.first
        count = 0
        if i == 0:
          self.first = self.first.next
          return
        while curr != None:
            if count == i:
              if curr.next == None:
                self.last = curr
              old.next = curr.next
              break
            old = curr
            curr = curr.next
            count += 1


# переворот

def reverse_(self):
        prev = None
        cur_node = self.head
        next_ = None
        while cur_node is not None:
            next_ = cur_node.get_next() # выбираем следующее
            cur_node.set_next(prev) # следующим делаем предыдущее
            prev = cur_node # предыдущее сдвигаем на текущее
            cur_node = next_ # а текущее передвигаем на следующее
        self.head = prev
        return
