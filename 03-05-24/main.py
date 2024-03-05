import asyncio

class TcpConnector(asyncio.Transport):
    def connection_made(self, transport: asyncio.Transport):
        transport.close()
    def connection_lost(self, exc):
        pass

async def try_connect(ip, port):
    loop = asyncio.get_running_loop()
    await asyncio.wait_for(loop.create_connection(TcpConnector, ip, port), .05)
    return port
    
async def main():
    ip = '127.0.0.1'
    portrange = (130, 140)
    loop = asyncio.get_running_loop()
    
    ports_open = []
    coroutines = []
    def callback (coroutine):
        coroutines.remove(coroutine)
        try:
            print(coroutine.result())
        except (ConnectionRefusedError, TimeoutError, PermissionError):
            pass
    
    for port in range(*portrange):
        # print(f"scanning {port}")
        # try:
        coroutines.append(loop.create_task(try_connect(ip, port)))
        coroutines[-1].add_done_callback(callback)
            # loop.create_task(try_connect(ip,port)).
        # except (ConnectionRefusedError, TimeoutError, PermissionError):
            # pass
        # else:
            # ports_open.append(port)
    while len(coroutines)>0:
        await asyncio.sleep(1)
    
    
    # print(ports_open)
        

asyncio.run(main())