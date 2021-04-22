import urllib.parse as parse
import time
import asyncio
import websockets
import json

from gpio.config import outputs
from gpio.interface import setup
from gpio.interface import cleanup

connections = []

async def handle_live(websocket, path):
    while True:
        if websocket not in connections:
            connections.append(websocket)
        request = await websocket.recv()
        parsed = json.loads(request)
        print("< {}".format(request))

        for conn in connections:
            await conn.send(json.dumps(parsed))

if __name__ == "__main__":
    try:
        setup(outputs)
        start_server = websockets.serve(handle_live, '0.0.0.0', 8082)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        cleanup()

    print("Server stopped.")