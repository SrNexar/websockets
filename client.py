import asyncio
import websockets

async def send_message():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            # Envía un mensaje al servidor
            message = input("Ingrese un mensaje: ")
            await websocket.send(message)
            
            # Espera la respuesta del servidor
            response = await websocket.recv()
            print(f"Respuesta del servidor: {response}")

asyncio.get_event_loop().run_until_complete(send_message())
