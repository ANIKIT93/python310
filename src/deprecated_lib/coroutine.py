import sys


# Deprecated: Use 'asyncio' or 'trio' for coroutine management instead.
def coroutine_depth(depth):
    sys.set_coroutine_origin_tracking_depth(depth)
    return True


if __name__ == "__main__":
    coroutine_depth(5)
