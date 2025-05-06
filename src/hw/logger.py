import logging


logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.DEBUG,
    handlers=[logging.FileHandler("program.log"), logging.StreamHandler()],
)


def logger(message: str) -> None:
    logging.info(message)
