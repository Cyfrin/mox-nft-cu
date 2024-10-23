"""
@ version 0.4.0
@ title: Basic NFT
@ license: MIT
"""
from snekmate.tokens import erc721
from snekmate.auth import ownable as ow

initializes: ow
initializes: erc721[ownable := ow]

exports: erc721.__interface__

# ------------------------------------------------------------------
#                        STATE VARIABLES
# ------------------------------------------------------------------
NAME: constant(String[9]) = "Puppy NFT"
SYMBOL: constant(String[4]) = "PNFT"
BASE_URI: constant(String[7]) = "ipfs://"
EIP_712_VERSION: constant(String[1]) = "1"


# ------------------------------------------------------------------
#                       EXTERNAL FUNCTIONS
# ------------------------------------------------------------------
@deploy
def __init__():
    ow.__init__()
    erc721.__init__(NAME, SYMBOL, BASE_URI, NAME, EIP_712_VERSION)


@external
def mint(uri: String[432]):
    token_id: uint256 = erc721._counter
    erc721._counter = token_id + 1
    erc721._safe_mint(msg.sender, token_id, b"")
    erc721._set_token_uri(token_id, uri)


@external
def get_base_uri() -> String[7]:
    return BASE_URI
