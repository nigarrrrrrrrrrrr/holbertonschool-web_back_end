#!/usr/bin/env python3
"""
Bu modul eyni vaxtda icra olunan asinxron coroutine-ləri idarə edir.
Burada wait_n funksiyası vasitəsilə çox sayda tapşırıq işə salınır.
"""
import asyncio
from typing import List

# wait_random funksiyasını verilən tapşırığa uyğun idxal edirik
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    n dəfə wait_random coroutine-ni çağırır və nəticələri
    hazır olma ardıcıllığına (artan sıra) uyğun olaraq qaytarır.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    
    # as_completed(tasks) siyahıdakı tapşırıqları bitdikcə qaytarır
    delays = [await task for task in asyncio.as_completed(tasks)]
    
    return delays
    
