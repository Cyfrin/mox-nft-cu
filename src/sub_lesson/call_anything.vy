# pragma version 0.4.1
"""
@license GPL-3.0-or-later
@title Mood NFT
"""

some_address: public(address)
amount: public(uint256)


@external
def transfer(to: address, amount: uint256):
    self.some_address = to
    self.amount = amount


@external
@view
def get_selector_one() -> bytes4:
    return self._get_selector_one()


@internal
@view
def _get_selector_one() -> bytes4:
    return method_id("transfer(address,uint256)", output_type=bytes4)


@internal
@view
def _get_data_to_call_transfer(
    some_address: address, amount: uint256
) -> Bytes[100]:
    return abi_encode(
        self.some_address,
        self.amount,
        method_id=method_id("transfer(address,uint256)", output_type=bytes4),
    )


@external
@view
def get_data_to_call_transfer(
    some_address: address, amount: uint256
) -> Bytes[100]:
    return self._get_data_to_call_transfer(some_address, amount)


@external
def call_transfer_function_directly(some_address: address, amount: uint256):
    data: Bytes[100] = self._get_data_to_call_transfer(some_address, amount)
