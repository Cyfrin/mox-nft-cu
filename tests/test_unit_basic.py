from script.deploy_basic_nft import PUG_URI


def test_initialized_correctly(basic_nft):
    assert basic_nft.name() == "Puppy NFT"
    assert basic_nft.symbol() == "PNFT"


def test_minted_sets_uri(basic_nft):
    basic_nft.mint(PUG_URI)
    assert basic_nft.tokenURI(1) == basic_nft.get_base_uri() + PUG_URI
