import threading, asyncio, time, random

def reply(customer):
    print(f"[Threading] Replying to {customer}...")
    time.sleep(2)
    print(f"[Threading] {customer} query solved!")

def threading_example():
    customers=["C1","C2","C3"]
    threads=[threading.Thread(target=reply,args=(c,)) for c in customers]
    [t.start() for t in threads]; [t.join() for t in threads]

async def async_reply(customer):
    print(f"[Asyncio] Replying to {customer}...")
    await asyncio.sleep(2)
    print(f"[Asyncio] {customer} query solved!")

async def asyncio_example():
    customers=["C1","C2","C3"]
    await asyncio.gather(*[async_reply(c) for c in customers])

if __name__=="__main__":
    threading_example()
    asyncio.run(asyncio_example())
