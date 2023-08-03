from tkinter import *
import websocket,json,time,base64,os
from printer import print_text_unix

root = Tk()
root.title("Bill Printer")
root.geometry("925x500+300+200")

def on_message(ws,messages):
    try:
        message= json.loads(messages)
        print("******",message)
        printer_name = message["name"]
        data = base64.b64decode(message["data"])
        with open("printing_file.pdf","wb") as file:
            file.write(data)
        file_name="printing_file.pdf"    
        print_text_unix(file_name,printer_name)
        os.remove(file_name)

    
    except Exception as e:
        print("Error: ",e)

def sendToServer():
    websocket.enableTrace(False)
    while True:
        try:
            ws = websocket.WebSocketApp("ws://localhost:8002",on_message = on_message)
            
            ws.run_forever()
        
        except Exception as e:
            print("an error occured: ", str(e))
            time.sleep(5)
sendToServer()

root.withdraw()
root.mainloop()