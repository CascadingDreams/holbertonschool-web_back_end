#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random
wait_random_2 = __import__('0-basic_async_syntax').wait_random_2

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random_2(5)))
print(asyncio.run(wait_random(15)))