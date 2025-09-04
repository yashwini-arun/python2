import threading, asyncio, time, random

def send_notification(user):
    print(f"[Threading] Notifying {user}...")
    time.sleep(2)
    print(f"[Threading] Notification sent to {user}")

def threading_example():
    users=["U1","U2","U3"]
    threads=[threading.Thread(target=send_notification,args=(u,)) for u in users]
    [t.start() for t in threads]; [t.join() for t in threads]

async def async_notify(user):
    print(f"[Asyncio] Notifying {user}...")
    await asyncio.sleep(2)
    print(f"[Asyncio] Notification sent to {user}")

async def asyncio_example():
    users=["U1","U2","U3"]
    await asyncio.gather(*[async_notify(u) for u in users])

if __name__=="__main__":
    threading_example()
    asyncio.run(asyncio_example())
