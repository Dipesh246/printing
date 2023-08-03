import asyncio
import websockets,json, base64


file =  open("DBMS_Assignment1.pdf", "rb")
file_content = file.read()
# print(file_content)

file_content_base64=base64.b64encode(file_content).decode("utf-8")

async def websocket_server(websocket, path):
    print("Client connected!")

    try:
        while True:
            data = {
                "name":"Brother_DCP_L2540DW_series",
                "data":file_content_base64
            }
            print(data)
            await websocket.send(json.dumps(data))
            await asyncio.sleep(5)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected!")

start_server = websockets.serve(websocket_server, "localhost", 8002)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
