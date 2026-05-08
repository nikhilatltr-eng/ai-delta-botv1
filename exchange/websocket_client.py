# exchange/websocket_client.py

import asyncio
import websockets
import json

from config.settings import WS_URL

class DeltaWebSocket:

    async def connect(self):

        async with websockets.connect(
            WS_URL
        ) as ws:

            payload = {
                "type": "subscribe",
                "payload": {
                    "channels": [
                        {
                            "name": "all_trades",
                            "symbols": ["ETHUSDT"]
                        },
                        {
                            "name": "l2_orderbook",
                            "symbols": ["ETHUSDT"]
                        }
                    ]
                }
            }

            await ws.send(
                json.dumps(payload)
            )

            while True:

                data = await ws.recv()

                print(data)