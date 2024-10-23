from moccasin.config import get_active_network

TOKEN_TO_FLIP = 0


def flip_mood():
    active_network = get_active_network()
    mood_nft_contract = active_network.manifest_named("mood_nft")
    mood_nft_contract.flip_mood(TOKEN_TO_FLIP)
    print(f"Flipped mood NFT on {active_network.name}")
    print(mood_nft_contract.tokenURI(TOKEN_TO_FLIP))


def moccasin_main():
    flip_mood()
