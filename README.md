# zeroIP

## Problem statement

A cryptocurrency transaction is broadcast by a user sending a signed message to
several nodes that propagate it through the network via the mempool  —  until a miner
includes it in a block.

This propagation of the transaction is often done via the open internet. As a
side effect, users silmuntaneously leak their IP addreses, & this makes  it possible to decode
metadata such as physical location, timezone etc for both the sender, recipients, miners
& node operators.

Even if the users are transacting in  privacy currencies like Zcash, Monero, Grin or
using tumblers, the problem still persists.
This is because the IP address leakage problem exists in the neworking layer of the app
and not the blockchain's data layer.
Users can be tracked by analysing IP addresses of  transaction broadcasts on the open internet as elaborated by several researchers[^1]

## Solution

zeroIP is an api interface that allows cryptocurrency transactions to be sent to miners
without leaking  IP addreses.

It acheives this by proxing transactions through the Nym Anonymity Mixnet[^2].
The Nym mixnet propergates data packets in a provably secure cryptographic format called Sphinx.
The Sphinx format encrypts packet size/length, packet origin & packet destination[^3].

This allows node operators, miners  & wallet users to securely propergate transactions amongst
each other without revealing metadata like physical location, timezone etc.
zeroIP inheritly acts as a proxy server or VPN servce for crypto payments.

## Usage

zeroIP can be used in two ways. The first way is by allowing wallet users to explicitly broadcast transactions through an API provided by zeroIP (similar to [Wallet Connect](https://walletconnect.org/)).
The second way is by hosting an simple web inteface where users can broadcast transactions by pasting the transaction
payload in to a form (similar to Ether Scan's [pushTx](https://etherscan.io/pushTx)).

### Footnotes

[^1]: [An Analysis of Anonymity in Bitcoin Using P2PNetwork Traffic](https://www.freehaven.net/anonbib/cache/bitcoin-p2p-anon.pdf), [Transaction Clustering Using Network Traffic Analysis for Bitcoin and Derived Blockchains](https://orbilu.uni.lu/bitstream/10993/39728/1/biryukov-tikhomirov-transaction-clustering.pdf)

[^2]: [The Nym Mixnet](https://nymtech.net/)
[^3]: [Sphinx: The anonymous data format behind Lightning and Nym](https://medium.com/nymtech/sphinx-tl-dr-the-data-packet-that-can-anonymize-bitcoin-and-the-internet-18d152c6e4dc)
