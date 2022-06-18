import logging as logger
import random
import string


def generate_random_email_and_password(domain=None, email_prefix=None):
    logger.debug('Generating random email and pass')
    if not domain:
        domain = "karso.com"
    if not email_prefix:
        email_prefix = "testuser"

    random_email_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_length))

    email = email_prefix + '_' + random_string + '@' + domain
    password_length = 20
    random_password = ''.join(random.choices(string.ascii_lowercase, k=password_length))

    random_info = {'email' : email, 'password': random_password}

    logger.debug(f"Randomly generated email and password are {random_info}")

    return random_info


def generate_random_string(length=10, prefix=None, suffix=None):

    random_string = ''.join(random.choices(string.ascii_lowercase, k=length))

    if prefix:
        random_string = prefix + random_string
    if suffix:
        random_string = random_string + suffix

    return random_string