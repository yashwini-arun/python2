import threading, asyncio, time, random

def monitor(patient):
    print(f"[Threading] Monitoring {patient}...")
    time.sleep(2)
    print(f"[Threading] {patient} stable")

def threading_example():
    patients=["Pat1","Pat2","Pat3"]
    threads=[threading.Thread(target=monitor,args=(p,)) for p in patients]
    [t.start() for t in threads]; [t.join() for t in threads]

async def async_monitor(patient):
    print(f"[Asyncio] Monitoring {patient}...")
    await asyncio.sleep(2)
    print(f"[Asyncio] {patient} stable")

async def asyncio_example():
    patients=["Pat1","Pat2","Pat3"]
    await asyncio.gather(*[async_monitor(p) for p in patients])

if __name__=="__main__":
    threading_example()
    asyncio.run(asyncio_example())
