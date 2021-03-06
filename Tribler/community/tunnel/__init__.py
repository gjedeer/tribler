"""
The Tunnel community package

Defines a ProxyCommunity which discovers other proxies and offers an API to
create and reserve circuits. A basic SOCKS5 server is included which reserves
circuits for its client connections and tunnels UDP packets over them back and
forth
"""

from Tribler.community.privatesemantic.crypto.optional_crypto import mpz

ORIGINATOR = 0
EXIT_NODE = 1

CIRCUIT_TYPE_DATA = 'DATA'
CIRCUIT_TYPE_IP = 'IP'
CIRCUIT_TYPE_RP = 'RP'
CIRCUIT_TYPE_INTRODUCE = 'INTRODUCE'
CIRCUIT_TYPE_RENDEZVOUS = 'RENDEZVOUS'

CIRCUIT_STATE_READY = 'READY'
CIRCUIT_STATE_EXTENDING = 'EXTENDING'
CIRCUIT_STATE_TO_BE_EXTENDED = 'TO_BE_EXTENDED'
CIRCUIT_STATE_BROKEN = 'BROKEN'

PING_INTERVAL = 15.0
# we use the 1024 bit modulus from rfc2409
# http://tools.ietf.org/html/rfc2409#section-6.2
DIFFIE_HELLMAN_GENERATOR = 2
DIFFIE_HELLMAN_MODULUS = mpz(0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381FFFFFFFFFFFFFFFF)
DIFFIE_HELLMAN_MODULUS_SIZE = 1024
