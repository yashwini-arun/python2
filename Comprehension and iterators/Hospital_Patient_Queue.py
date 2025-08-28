import logging, random
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

class PatientIDs:
    def __init__(self,limit): self.cur,self.limit=0,limit
    def __iter__(self): return self
    def __next__(self):
        if self.cur>=self.limit: raise StopIteration
        self.cur+=1; return f"P{self.cur:03d}"

patients = PatientIDs(5)
reports = {p: random.choice(["Critical","Stable","Recovering"]) for p in patients}
critical = [p for p,r in reports.items() if r=="Critical"]

logging.info(f"Patients: {reports}")
logging.info(f"Critical Cases: {critical}")
