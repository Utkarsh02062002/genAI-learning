import time


# Sync function
# def fetch_embedding_sync(chunk_id):
#     print(f"Starting chunk {chunk_id}")
#     time.sleep(1)
#     print(f"Finished chunk {chunk_id}")
#     return

# def main():
#     start_time = time.time()
#     results = []

#     for i in range(0,3):
#         results = fetch_embedding_sync(i)
#         print(f"Total time: {time.time() - start_time:.2f} seconds")

#     print(results)

# Async function
import asyncio

async def fetch_embedding_async(chunk_id):
    print(f"Starting chunk {chunk_id}")
    asyncio.sleep(1)
    print(f"Finished chunk {chunk_id}")
    return

async def main():
    start_time = time.time()
    
    results = await asyncio.gather(
    fetch_embedding_async(0),
    fetch_embedding_async(1),
    fetch_embedding_async(2)
    )

    print(f"Total time: {time.time() - start_time:.2f} seconds")


asyncio.run(main())