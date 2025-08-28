import logging, random
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(message)s")

class SeatNumbers:
    def __init__(self, total): self.cur, self.total = 0, total
    def __iter__(self): return self
    def __next__(self):
        if self.cur >= self.total:
            logging.debug("Reached seat limit.")
            raise StopIteration
        self.cur += 1
        seat = f"S{self.cur:02d}"
        logging.debug(f"Generated Seat: {seat}")
        return seat

try:
    seats = SeatNumbers(10)
    bookings = {s: random.choice(["Booked","Available"]) for s in seats}
    free = [s for s,v in bookings.items() if v=="Available"]

    logging.info(f"Bookings: {bookings}")

    if not bookings:
        logging.error("No bookings were generated!")
    if not free:
        logging.warning("No free seats available!")
    else:
        logging.info(f"Free Seats: {free}")

except Exception as e:
    logging.error(f"Unexpected Error: {e}")
