import logging


logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
# logging.disable(logging.CRITICAL)

logging.debug("program begins. with logging")
print("program begins. with print")

sum = 100

logging.debug("sum = {}".format(sum))

logging.debug("program ends. with logging")
print("program ends. with print")
