class Solution:
    # Write your code here
    def __init__(self):
          self.stack = []
          self.queue = []

    def pushCharacter(self, char):
          self.stack.append(char)

    def popCharacter(self):
          return(self.stack.pop(-1))

    def enqueueCharacter(self, char):
          self.queue.append(char)

    def dequeueCharacter(self):
        return(self.queue.pop(0))