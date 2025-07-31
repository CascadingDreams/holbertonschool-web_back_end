#!/usr/bin/env python3

'''
Task version of wait_n using task_wait_random
'''

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''calls task_wait_random n times and returns sorted delays'''
    tasks = [task_wait_random(max_delay) for i in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
