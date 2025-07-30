#!/usr/bin/env python3

'''Waits for a random delay between 0 and max_delay
seconds and eventually returns it at the same time'''

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''calls wait_random n num mof times'''
    tasks = [wait_random(max_delay) for i in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
