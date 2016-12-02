import hashlib


def actions(pwd):
    hash = hashlib.sha256()
    hash.update(pwd.encode('utf-8'))
    return hash.hexdigest()


if __name__ == '__main__':
    print(actions('112233'))
