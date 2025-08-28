import logging, random
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

class Days:
    def __init__(self,total): self.cur,self.total=0,total
    def __iter__(self): return self
    def __next__(self):
        if self.cur>=self.total: raise StopIteration
        self.cur+=1; return f"Day{self.cur}"

days = Days(7)
temps = {d: random.randint(20,40) for d in days}
hot = [d for d,t in temps.items() if t>30]

logging.info(f"Temperatures: {temps}")
logging.info(f"Hot Days: {hot}")
