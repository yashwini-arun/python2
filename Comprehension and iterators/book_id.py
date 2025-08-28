import logging, random
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

class BookIDs:
    def __init__(self, prefix, limit): self.prefix,self.num,self.limit=prefix,0,limit
    def __iter__(self): return self
    def __next__(self):
        if self.num>=self.limit: raise StopIteration
        self.num+=1; return f"{self.prefix}{self.num:03d}"

books = BookIDs("BK", 5)
library = {bid: random.randint(100, 500) for bid in books}
thick_books = [b for b,p in library.items() if p>300]

logging.info(f"Library: {library}")
logging.info(f"Thick Books: {thick_books}")
