import logging, random
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(message)s")

class EmployeeIDs:
    def __init__(self, limit): self.id, self.limit = 100, limit
    def __iter__(self): return self
    def __next__(self):
        if self.id >= self.limit:
            logging.debug("Reached employee limit.")
            raise StopIteration
        self.id += 1
        eid = f"E{self.id}"
        logging.debug(f"Generated Employee ID: {eid}")
        return eid

try:
    employees = EmployeeIDs(105)
    salaries = {eid: random.randint(20000,60000) for eid in employees}
    bonuses = {e: s+(0.1*s) for e,s in salaries.items()}

    if not salaries:
        logging.error("No salaries generated!")
    else:
        logging.info(f"Salaries: {salaries}")

    logging.info(f"With Bonus: {bonuses}")

except Exception as e:
    logging.error(f"Unexpected Error: {e}")
