import requests

from flask import Flask, response, jsonify
app = Flask(__name__)

# Initialize tx data
tx_data = {
    'network': 'none',
    'tx':'none'
}

# Index Page for ZeroIP
@app.route('/zeroIP')
def index():
    return '<a href="#">zeroIP</a>: A Nym Proxy Service For Crypto Payments.'

@app.route('/zeroIP/getTX')
def get_tx():
    # Initialize transaction status
    tx_status = {'sent': False, 'network': 'none'}

    # Get parameters for coin's network & tx blob
    network =  response.args('network')
    tx =  response.args('tx') # Get raw transaction in Hex 

    # Update tx data
    tx_data['network'] = network
    tx_data['tx'] = tx 

    send_tx = cast_tx(tx_data) # Send tx to respective network returns True if successful, False otherwise.

    # Update tx status
    if send_tx == True:
        tx_status['sent'] = True
        tx_status['network'] = network

    return jsonify(tx_status)

def cast_tx(message_data):
    message_data = tx_data

    # Broadcast tx to Mempool
    tx_sent = False

    # Send ETH tx 
    if message_data['network'] == 'ETH':
        r = requests.post('https://api.etherscan.io/api?module=proxy&action=eth_sendRawTransaction&hex={0}&apikey=YourApiKeyToken'.format(message_data['tx']))

        if r.status_code == 200: # Update tx status if successfully sent
            tx_sent = True

    return tx_sent # Returns True if tx is sent False otherwise

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

