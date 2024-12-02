class FlatIterator:
  def __init__(self, list_of_list):
     self.stack =[iter(list_of_list)]
  
  def __iter__(self):
     return self
  
  def __next__(self):
     while self.stack:
        try:
          cur_nested_list = next(self.stack[-1])
          if isinstance(cur_nested_list, list):
             self.stack.append(iter(cur_nested_list))
          else:
             return cur_nested_list
          
        except StopIteration:
           self.stack.pop()
        
     raise StopIteration