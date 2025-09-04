import threading, asyncio, time, random

def convert_pdf(file):
    print(f"[Threading] Converting {file}...")
    time.sleep(2)
    print(f"[Threading] {file} converted!")

def threading_example():
    files=["doc1.docx","doc2.docx","doc3.docx"]
    threads=[threading.Thread(target=convert_pdf,args=(f,)) for f in files]
    [t.start() for t in threads]; [t.join() for t in threads]

async def async_convert(file):
    print(f"[Asyncio] Converting {file}...")
    await asyncio.sleep(2)
    print(f"[Asyncio] {file} converted!")

async def asyncio_example():
    files=["doc1.docx","doc2.docx","doc3.docx"]
    await asyncio.gather(*[async_convert(f) for f in files])

if __name__=="__main__":
    threading_example()
    asyncio.run(asyncio_example())
