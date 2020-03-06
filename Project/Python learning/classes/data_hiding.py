class Justcounter:
   __secretCount= 0

   def count(self):
       self.__secretCount += 1
       print(self.__secretCount)

counter = Justcounter()
counter.count()
counter.count()
print(counter._Justcounter__secretCount) #_Justcounter jest klasą więc używając pełnej nazwy musimy wstawić "_" przed nazwę