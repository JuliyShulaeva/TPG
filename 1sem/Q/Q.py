class Node:
    def __init__(self, data=None, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


class B_Tree:
    def __init__(self, root=None, cur=None):
        self.root = root
        self.cur = cur
        self.stack = []

    def goto_root(self):
        self.cur = self.root
        self.stack = []

    def goto_left(self):
        self.stack.append(self.cur)
        self.cur = self.cur.left

    def goto_right(self):
        self.stack.append(self.cur)
        self.cur = self.cur.right


    def goto_parent(self):
        self.cur = self.stack.pop()

    def get_root(self):
        return self.root

    def insert(self, da):
        self.goto_root()
        # Новая вставка. Если дерево пусто, то создать корень
        if self.root is None:
            self.root=Node(da)
        else: # все по старому
            while (self.cur is not None) and (self.cur.data != da):
                if da > self.cur.data:
                    self.goto_right()
                else:
                    self.goto_left()
            if self.cur is None:
                self.goto_parent()
            new_node = Node(da, None, None)
            if da > self.cur.data:
                self.cur.right = new_node
            else:
                self.cur.left = new_node


    def to_sorted_list(self):
        lst=[]
        def cir(c): # рекурсивный обход.
            if c.right is not None:
                cir(c.right)
            lst.append(c.data)
            if c.left is not None:
                cir(c.left)
        cir(self.root)
        return lst



lst = [5, 7, 6, 8, 3, 4, 2]  # [int(n) for n in input().split()]
bt = B_Tree()

for x in lst:
    bt.insert(x)

sorted_list=bt.to_sorted_list()
print(sorted_list)
