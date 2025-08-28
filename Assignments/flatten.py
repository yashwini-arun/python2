import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(message)s")

def flatten(nested):
    """
    Generator function to flatten a nested list of arbitrary depth with logging.
    """
    if not isinstance(nested, list):
        logging.error(f"Expected list, got {type(nested)} instead!")
        return

    if not nested:
        logging.warning("Encountered an empty list.")

    for item in nested:
        if isinstance(item, list):
            logging.info(f"Found nested list: {item}")
            yield from flatten(item)   # Recursive flatten
        else:
            logging.debug(f"Yielding item: {item}")
            yield item

# Example usage
data = [1, [2, [3, 4], []], [5, [6, [7, [8, 9]]]], 10]

logging.info("Starting flattening process...")
try:
    for val in flatten(data):
        print(val, end=" ")
except Exception as e:
    logging.error(f"Unexpected error during flattening: {e}")
