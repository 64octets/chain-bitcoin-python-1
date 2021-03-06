from __future__ import absolute_import

import sure
from .. import Chain, NoApiKeyId, OpReturn, get_block_op_returns_by_height
from .mock_http_adapter import *


def test_get_block_op_returns_by_height():
    get_block_op_returns_by_height(block_height, api_key_id=api_key_id,
                                   http_adapter=http_adapter) \
        .should.equal(op_returns)


def test_get_block_op_returns_by_height_using_class():
    Chain(api_key_id=api_key_id, http_adapter=http_adapter) \
        .get_block_op_returns_by_height(block_height).should.equal(op_returns)


def test_get_block_op_returns_by_height_without_api_key_id():
    (lambda: get_block_op_returns_by_height(block_height,
                                            http_adapter=no_http())) \
        .should.throw(NoApiKeyId)


block_height = 308920

api_key_id = 'DEMO-4a5e1e4'

url = 'https://api.chain.com/v1/bitcoin/blocks/308920/op-returns' \
      '?api-key-id=DEMO-4a5e1e4'

response_body = """
[
  {
    "transaction_hash":"ac88...",
    "hex":"4067...",
    "text":"Yo Adam!",
    "sender_addresses": ["1Bj5..."],
    "receiver_addresses": ["1def..."]
  },
  {
    "transaction_hash":"5d7...",
    "hex":"4052...",
    "text":"Hey Devon, what's up?",
    "sender_addresses": ["1def..."],
    "receiver_addresses": ["1Bj5..."]
  }
]
"""

op_returns = [
    OpReturn(
        transaction_hash='ac88...',
        hex='4067...',
        text='Yo Adam!',
        sender_addresses=['1Bj5...'],
        receiver_addresses=['1def...'],
    ),
    OpReturn(
        transaction_hash='5d7...',
        hex='4052...',
        text='Hey Devon, what\'s up?',
        sender_addresses=['1def...'],
        receiver_addresses=['1Bj5...'],
    ),
]

http_adapter = mock_get(url, response_body)
