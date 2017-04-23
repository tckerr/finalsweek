enabled = True


def log(*args):
    if enabled:
        print(*args)
