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
Users can be tracked by analysing IP addresses of  transaction broadcasts on the open internet. 


## Solution

zeroIP is an api interface that allows cryptocurrency transactions to be sent to miners 
without leaking  IP addreses.

It acheives this by proxing transactions through the Nym Anonymity Mixnet. 
The Nym mixnet propergates data packets in a provably secure cryptographic format called sphinx.
Sphinx encrypts packet size/length, packet origin & packet destination. 

This allows node operators, miners  & wallet users to securely propergate transactions amongst
each other without revealing metadata like physical location, timezone etc.
	