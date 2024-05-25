import asyncio
import websockets
import os

async def handle_client(websocket, path):
    while True:
        try:
            message = await websocket.recv()
            print(f"Mensaje recibido del cliente: {message}")
            response = f"Mensaje recibido: {message}"
            await websocket.send(response)
        except websockets.ConnectionClosed:
            print("Conexión cerrada")
            break

# Heroku asigna un puerto a través de la variable de entorno PORT
port = int(os.environ.get('PORT', 8765))
start_server = websockets.serve(handle_client, "0.0.0.0", port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
