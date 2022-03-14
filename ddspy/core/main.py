from box import Box
from copy import deepcopy

class Dlist():
    def __init__(self, none_value=None):
        self.list = []
        self.none_value = none_value
    
    def __call__(self):
        return self.list
    
    def __repr__(self):
        return f'{self.list}'
    
    def __str__(self):
        return f'{self.list}'
    
    def __setitem__(self, item, value):
        try:
            self.list[item] = value
        except:
            for _ in range(item - len(self.list)+1):
                self.list.append(deepcopy(self.none_value))
            self.list[item] = value
    
    def __getitem__(self, item):
        try:
            return self.list[item]
        except IndexError:
            return deepcopy(self.none_value)
        

class Ddict():
    def __init__(self, none_value=None):
        self.list = []
        self.none_value = none_value
    
    def __call__(self):
        return self.list
    
    def __repr__(self):
        return f'{self.list}'
    
    def __str__(self):
        return f'{self.list}'
    
    def __setitem__(self, item, value):
        self.list.append(Box(dict(item=value)))
        
    def __getitem__(self, item):
        try:
            return self.list[item]
        except IndexError:
            for _ in range(item-len(self.list)+1):
                self.list.append(Box(dict()))
            return self.list[item]



