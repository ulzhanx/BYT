class ReusablePool:
   
    dictionary = list()

    def __init__(self):
        pass

    def acquire(self):
        return self.dictionary.pop()

    def release(self, reusable):
        return self.dictionary.append(reusable)


class Reusable:
  

    pass




if __name__ == "__main__":
    
    new1 = ReusablePool()
    new2 = ReusablePool()
    
    new1.release(10)
    new2.release(20)
    
    new1.acquire()
    new2.acquire()
    
    
    