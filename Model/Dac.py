import DbConnect
class Dac() :
    def __init__(self) -> None:
        self.conn = DbConnect().connect()
        
    def insert(self, query) :
        pass
    def selectData(self, query) : 
        pass
    def delete(self,query) : 
        pass
    def update(self,query) : 
        pass