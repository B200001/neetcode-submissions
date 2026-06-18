class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.left = LinkedNode("")
        self.right = LinkedNode("")
        self.curr = LinkedNode(homepage)
        self.left.next = self.curr
        self.curr.prev = self.left
        self.right.prev = self.curr
        self.curr.next = self.right
        

    def visit(self, url: str) -> None:
        temp = LinkedNode(url)
        self.curr.next = temp
        temp.prev = self.curr
        temp.next = self.right
        self.right.prev = temp
        self.curr = temp

        

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev != self.left:
            self.curr = self.curr.prev
            steps -= 1
        
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next != self.right:
            self.curr = self.curr.next
            steps -= 1
        
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)