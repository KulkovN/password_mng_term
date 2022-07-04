import secrets
import string


APLPHABET = string.ascii_letters + string.digits


def pwdGen(length:int, abcd = APLPHABET) -> str:
    """Simple pwd generator

    :param length: length of password to like
    :param abcd: defaults to APLPHABET
    :return: string of password
    """
    return str(''.join(secrets.choice(abcd) for i in range(int(length))))  # for a 20-character password

