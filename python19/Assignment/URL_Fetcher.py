import threading
import requests
import asyncio
import aiohttp
import time
import ssl, certifi

# ---------------- URLs ----------------
urls = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/3",
    "https://httpbin.org/delay/1"
]

# ---------------- Threading Example ----------------
def fetch_url_thread(url):
    print(f"[Threading] Fetching {url}")
    resp = requests.get(url)
    print(f"[Threading] Done {url}, status={resp.status_code}")

def threading_example():
    start = time.time()
    threads = [threading.Thread(target=fetch_url_thread, args=(u,)) for u in urls]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print(f"[Threading] Finished in {time.time() - start:.2f}s\n")

# ---------------- Asyncio Example ----------------
ssl_context = ssl.create_default_context(cafile=certifi.where())

async def fetch_url_async(session, url):
    print(f"[Asyncio] Fetching {url}")
    async with session.get(url, ssl=ssl_context) as resp:
        print(f"[Asyncio] Done {url}, status={resp.status}")

async def asyncio_example():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url_async(session, u) for u in urls]
        await asyncio.gather(*tasks)
    print(f"[Asyncio] Finished in {time.time() - start:.2f}s\n")

# ---------------- Main ----------------
if __name__ == "__main__":
    print("=== Threading Version ===")
    threading_example()

    print("=== Asyncio Version ===")
    asyncio.run(asyncio_example())
