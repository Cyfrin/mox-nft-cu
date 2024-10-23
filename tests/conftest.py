import pytest

from script.deploy_basic_nft import deploy_basic_nft
from script.deploy_mood_nft import deploy_mood_nft
from script.deploy_sub_lesson import (
    deploy_call_anything,
    deploy_encoding,
    deploy_raw_call,
)


@pytest.fixture
def basic_nft():
    return deploy_basic_nft()


@pytest.fixture
def call_anything():
    return deploy_call_anything()


@pytest.fixture
def encoding():
    return deploy_encoding()


@pytest.fixture
def raw_call():
    return deploy_raw_call()


@pytest.fixture
def mood_nft():
    return deploy_mood_nft()
