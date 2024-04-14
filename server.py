import asyncio
from flask import Flask
import asyncio_dgram


async def udp_echo_server():
    stream = await asyncio_dgram.bind(("35.160.120.126", 8888))

    print(f"Serving on {stream.sockname}")
    list_of_connections = []
    while True:
        data, remote_addr = await stream.recv()
        print(f"Echoing {data.decode()!r}")
        list_of_connections.append(remote_addr)
        for addr in list_of_connections:
            await stream.send(data,addr)

    await asyncio.sleep(0.5)
    print(f"Shutting down server")
    

def main():
    loop = asyncio.get_event_loop()
    loop.create_task(udp_echo_server())
    t = threading.Thread(target=lambda:Flask().run(port=80))
    loop.run_forever()

if __name__ == "__main__":
    asyncio.run(main())
