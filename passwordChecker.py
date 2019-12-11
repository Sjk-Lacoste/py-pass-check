import re
import logging


logging.basicConfig(filename = "app.log", level = logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s", datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger()


def password_is_valid(password):
    if password == '':
        logger.error("Password cannot be empty")
        raise Exception("Password must not be empty")
    else:
        logger.info("Password is not empty")

    if len(password) < 8:
        logger.error("Password should at least be 8 characters or longer")
        raise Exception("Password must at least be 8 characters or longer")
    else:
        logger.info("Password is at least 8 charaters long")

    if not re.search(r'[a-z]', password):
        logger.error("Password must at least have lowercase character or more")
        raise Exception("Password must at least have lowercase character or more")
    else:
        logger.info("Password contains at least one lowercase")

    if re.search('[A-Z]', password):
        logger.info("Password contains atleast one uppercase charater")
    else:
        logger.error("Password must at least one uppercase character or more.")
        raise Exception("Password must at least one uppercase character or more.")

    if re.search(r'[0-9]', password):
        logger.info("Password contains at least one digit")
    else:
        logger.error("Password must at least contain one digit or more")
        raise Exception("Password must contain at least one digit or more")

    if re.search(r'[!@#$%&><|{}].{1,}', password):
        logger.info("Password contains atleast one special character")
    else:
        logger.exception("Password must contain at least one special character")
        raise Exception("Password must contain at least one special character")

    return password


def password_is_ok(password):
    if not password == '' and len(password) > 8:
        if re.search(r'[a-z]', password) or re.search(r'[A-Z]', password) or re.search(r'[0-9]') or re.search(r'[!@#$%&><|{}].{1,}', password):
            logger.info("Password is ok!")
            return True
    else:
        logger.error("Password is never ok")
        return False



