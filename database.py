class Database:
   def __init__(self,toto):
       self.toto = toto
       for i in self.toto:
          print(i.name, i.url)