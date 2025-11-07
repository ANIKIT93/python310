import asyncio


def async_example():
    loop = asyncio.get_event_loop()
    print(loop)
    return True


if __name__ == "__main__":
    async_example()
