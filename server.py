import asyncio
import websockets

# Función para manejar las conexiones de los clientes
async def handle_client(websocket, path):
    while True:
        # Espera un mensaje del cliente
        message = await websocket.recv()
        print(f"Mensaje recibido del cliente: {message}")

        # Envía un mensaje de respuesta al cliente
        response = f"Mensaje recibido: {message}"
        await websocket.send(response)

# Configura el servidor WebSocket
start_server = websockets.serve(handle_client, "localhost", 8765)

# Inicia el servidor
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
