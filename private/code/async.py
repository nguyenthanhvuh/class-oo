import asyncio
import time

async def say_after(delay, message):
    await asyncio.sleep(delay)  # Simulate a non-blocking delay
    print(message)

async def main():
    print("Start")
    await say_after(1, "Hello")
    await say_after(2, "World")
    print("End")

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())  # Run the main coroutine
    print(f"Execution time: {time.time() - start_time:.2f} seconds")