

from merkle import MerkleTree
from nacl.encoding import RawEncoder
from nacl.hash import sha256
from binascii import hexlify
from random import randint


messages = [b'hello world', b'world hello', b'BTC', b'ETH', b'XLM', b'RawEncoder', b'encoder', b'sha256']

leaves = [sha256(messages[i], encoder=RawEncoder) for i in range(len(messages))]

print("Messages: ", messages)
print()

print("MerkleTree:")
m = MerkleTree.from_leaves(leaves)

m.print_hex()
print()

index = randint(0, len(messages)-1)
print("Proof that message ", messages[index], "(", str(hexlify(leaves[index])), ") is part of the tree:")
proof = m.prove(messages[index])
MerkleTree.print_hex_proof(proof)
print()

print("Proof verified" if MerkleTree.verify(messages[index], proof) else "Proof failed verification")