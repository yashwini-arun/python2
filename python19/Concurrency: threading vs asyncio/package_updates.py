import threading, asyncio, time, random

def deliver(pkg):
    print(f"[Threading] Delivering {pkg}...")
    time.sleep(2)
    print(f"[Threading] {pkg} delivered!")

def threading_example():
    pkgs=["P1","P2","P3"]
    threads=[threading.Thread(target=deliver,args=(p,)) for p in pkgs]
    [t.start() for t in threads]; [t.join() for t in threads]

async def async_deliver(pkg):
    print(f"[Asyncio] Delivering {pkg}...")
    await asyncio.sleep(2)
    print(f"[Asyncio] {pkg} delivered!")

async def asyncio_example():
    pkgs=["P1","P2","P3"]
    await asyncio.gather(*[async_deliver(p) for p in pkgs])

if __name__=="__main__":
    threading_example()
    asyncio.run(asyncio_example())
