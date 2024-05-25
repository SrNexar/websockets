import asyncio
import websockets

async def send_message():
    uri = "ws://<websockets1>.herokuapp.com"  # Reemplaza <nombre-de-tu-aplicacion> con el nombre de tu aplicación Heroku
    async with websockets.connect(uri) as websocket:
        message = "Mensaje automático desde el cliente"
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Respuesta del servidor: {response}")

if __name__ == "__main__":
    asyncio.run(send_message())
