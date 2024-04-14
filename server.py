"""
import asyncio

class DiscoveryProtocol(asyncio.DatagramProtocol):
    def __init__(self):
        super().__init__()
    def connection_made(self, transport):
        self.transport = transport
    def datagram_received(self, data, addr):
        print(data)

def start_discovery():
    loop = asyncio.get_event_loop()
    t = loop.create_datagram_endpoint(DiscoveryProtocol,local_addr=('0.0.0.0',8100))
    loop.run_until_complete(loop.run_forever())

def run_server():
    asyncio.run(start_discovery())

if __name__ == '__main__':
    asyncio.run(start_discovery())
"""
import asyncio

import asyncio_dgram
import asyncio
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
    #t = threading.Thread(target=lambda:App().mainloop())
    loop.run_forever()

if __name__ == "__main__":
    asyncio.run(main())
