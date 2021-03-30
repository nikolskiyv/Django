class CustomList(list):
    def __add__(self, list):
        list_copy = list[:]
        self_copy = CustomList(self)
        if len(list_copy) > len(self_copy):
            self_copy.extend([0 for i in range(abs(len(self)-len(list)))])
        else:
            list_copy.extend([0 for i in range(abs(len(self)-len(list)))])
        for i in range(len(list_copy)):
            self_copy[i] += list_copy[i]
        return self_copy
    
    def __sub__(self, list):
        list_copy = list[:]
        self_copy = CustomList(self)
        if len(list_copy) > len(self_copy):
            self_copy.extend([0 for i in range(abs(len(self)-len(list)))])
        else:
            list_copy.extend([0 for i in range(abs(len(self)-len(list)))])
        for i in range(len(list_copy)):
            self_copy[i] -= list_copy[i]
        return self_copy 
    
    def __radd__(self, list):
        return self + list
            
    def __rsub__(self, list):
        list_copy = list[:]
        self_copy = CustomList(self)
        if len(list_copy) > len(self_copy):
            self_copy.extend([0 for i in range(abs(len(self)-len(list)))])
        else:
            list_copy.extend([0 for i in range(abs(len(self)-len(list)))])
        for i in range(len(list_copy)):
            list_copy[i] -= self_copy[i]
        return list_copy    
    
    def list_sum(self, list):
        sum = 0
        for i in range(len(list)):
            sum += list[i]   
        return sum
    
    def __lt__(self, list):
        return True if self.list_sum(self) < self.list_sum(list) else False
    
    def __le__(self, list):
        return True if self.list_sum(self) <= self.list_sum(list) else False
    
    def __eq__(self, list):
        return True if self.list_sum(self) == self.list_sum(list) else False
    
    def __ne__(self, list):
        return True if self.list_sum(self) != self.list_sum(list) else False
    
    def __gt__(self, list):
        return True if self.list_sum(self) > self.list_sum(list) else False
    
    def __ge__(self, list):
        return True if self.list_sum(self) >= self.list_sum(list) else False
