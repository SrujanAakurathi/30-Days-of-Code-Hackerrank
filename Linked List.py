def insert(self,head,data):
        temp = Node(data)
        if head is None:
            head = temp
        else:
            curr = head
            while curr.next:
                curr = curr.next
            curr.next = temp
        return head