import websocket, requests

try:
    import thread
except ImportError:
    import _thread as thread
import time

# Listen for Ethereum transactions on the Nym Network
def on_message(ws, message):
    r = requests.post('https://zeroIP-api-server:8090/zeroIP/getTX?network=ETH&tx={0}'.format(message))

    if r.status_code == 200:
        print("Transaction sent to Ethereum network") # log the fact that a transaction was picked up & propergated

    print(message)

# Show connection errors
def on_error(ws, error):
    print(error)

## Call back the the connection is closed 
def on_close(ws):
    print("### closed ###")

# Open web socket channel connection
def on_open(ws):
    def run(*args):
        for i in range(10): # choose how many seconds you want the web socket session to ran for
            time.sleep(1)
            ws.send("Running session for %d seconds" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://nym-mix-node:9001/mix/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()