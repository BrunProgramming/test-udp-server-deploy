import asyncio
import threading
from flask import Flask
import asyncio_dgram


async def udp_echo_server():
    stream = await asyncio_dgram.bind(("127.0.0.1", 8888))

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
    t = threading.Thread(target=lambda:Flask(__name__).run(port=80))
    t.start()
    loop.run_forever()

if __name__ == "__main__":
    asyncio.run(main())
