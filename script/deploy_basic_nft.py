from moccasin.boa_tools import VyperContract

from src import basic_nft

PUG_URI = "QmW16U98JrY9HBY36rQtUuUtDnm6LdEeNdAAggmrx3thMa"


def deploy_basic_nft() -> VyperContract:
    basic_nft_contract = basic_nft.deploy()
    print(f"Deployed basic NFT to {basic_nft_contract.address}")
    basic_nft_contract.mint(PUG_URI)
    print(f"Minted Pug NFT with URI {basic_nft_contract.tokenURI(0)}")
    return basic_nft_contract


def moccasin_main():
    return deploy_basic_nft()
