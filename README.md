# mainnet
A developer friendly bitcoin cash wallet api

This API is currently in *active* development, breaking changes may
be made prior to official release of version 1.0.0.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.1.21
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/mainnet-cash/mainnet-python-generated.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/mainnet-cash/mainnet-python-generated.git`)

Then import the package:
```python
import mainnet
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import mainnet
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import mainnet
from mainnet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest-unstable.mainnet.cash
# See configuration.py for a list of all supported configuration parameters.
configuration = mainnet.Configuration(
    host = "https://rest-unstable.mainnet.cash"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = mainnet.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)


# Enter a context with an instance of the API client
with mainnet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mainnet.ContractApi(api_client)
    contract_fn_request = {"contractId":"testnet:TURNME1UQmxaakEwT0dJelpHRXpOVEUzT1RObU5tVmtNVFJqWXpKbVpHVTBOakJpWldOak5XSTJOVGhrT1RFek9EUTBNMkk1WVRNd01EQTNNRGRoTm1FMzpNRE0wT1RjNFlXTTBOalJtTXpVNFlqSXpOV1l4TVRJeE1tVmlObVV3TVRkaFpqa3dNakUxWWprd1lqRm1aamMwTnpGa09XRmxNbUZpWWpWbE1Ea3lOak5pOk1qRTE=:Y29udHJhY3QgVHJhbnNmZXJXaXRoVGltZW91dChwdWJrZXkgc2VuZGVyLCBwdWJrZXkgcmVjaXBpZW50LCBpbnQgdGltZW91dCkgewogICAgZnVuY3Rpb24gdHJhbnNmZXIoc2lnIHJlY2lwaWVudFNpZykgewogICAgICAgIHJlcXVpcmUoY2hlY2tTaWcocmVjaXBpZW50U2lnLCByZWNpcGllbnQpKTsKICAgIH0KCiAgICBmdW5jdGlvbiB0aW1lb3V0KHNpZyBzZW5kZXJTaWcpIHsKICAgICAgICByZXF1aXJlKGNoZWNrU2lnKHNlbmRlclNpZywgc2VuZGVyKSk7CiAgICAgICAgcmVxdWlyZSh0eC50aW1lID49IHRpbWVvdXQpOwogICAgfQp9Cg==:1996128042","action":"send","function":"timeout","to":{"unit":"sat","cashaddr":"bchtest:qpalhxhl05mlhms3ys43u76rn0ttdv3qg2usm4nm7t","value":2000},"feePerByte":1} # ContractFnRequest | Request a new cashscript contract

    try:
        # Call a method on a contract
        api_response = api_instance.contract_fn(contract_fn_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContractApi->contract_fn: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://rest-unstable.mainnet.cash*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ContractApi* | [**contract_fn**](docs/ContractApi.md#contract_fn) | **POST** /contract/call | Call a method on a contract
*ContractApi* | [**contract_info**](docs/ContractApi.md#contract_info) | **POST** /contract/info | Get information about a contract from the contractId
*ContractApi* | [**contract_utxos**](docs/ContractApi.md#contract_utxos) | **POST** /contract/utxos | List specific utxos on any contract
*ContractApi* | [**create_contract**](docs/ContractApi.md#create_contract) | **POST** /contract/create | Create a cashscript contract
*ContractEscrowApi* | [**create_escrow**](docs/ContractEscrowApi.md#create_escrow) | **POST** /contract/escrow/create | Create an escrow contract
*ContractEscrowApi* | [**escrow_fn**](docs/ContractEscrowApi.md#escrow_fn) | **POST** /contract/escrow/call | Finalize an escrow contract
*ContractEscrowApi* | [**escrow_info**](docs/ContractEscrowApi.md#escrow_info) | **POST** /contract/escrow/info | Get information about an escrow contract from the escrowContractId
*ContractEscrowApi* | [**escrow_utxos**](docs/ContractEscrowApi.md#escrow_utxos) | **POST** /contract/escrow/utxos | List specific utxos on any escrow contract
*FaucetApi* | [**get_addresses**](docs/FaucetApi.md#get_addresses) | **POST** /faucet/get_addresses | Get addresses to return back or donate the testnet bch and tokens 
*FaucetApi* | [**get_testnet_bch**](docs/FaucetApi.md#get_testnet_bch) | **POST** /faucet/get_testnet_bch | Get testnet bch 
*FaucetApi* | [**get_testnet_sbch**](docs/FaucetApi.md#get_testnet_sbch) | **POST** /faucet/get_testnet_sbch | Request testnet SmartBCH funds. The request is enqueued and served within 1-3 block confirmations. If the target address holds more that 0.1 BCH, the request will fail. Otherwise the address will be topped up to 0.1 BCH. 
*FaucetApi* | [**get_testnet_sep20**](docs/FaucetApi.md#get_testnet_sep20) | **POST** /faucet/get_testnet_sep20 | Request testnet SmartBch SEP20 tokens. The request is enqueued and served within 1-3 block confirmations. If the target address holds more that 10 tokens of requested kind, the request will fail. Otherwise the address will be topped up to 10 tokens. 
*FaucetApi* | [**get_testnet_slp**](docs/FaucetApi.md#get_testnet_slp) | **POST** /faucet/get_testnet_slp | Get testnet slp tokens 
*MineApi* | [**mine**](docs/MineApi.md#mine) | **POST** /mine | Mine regtest coins to a specified address
*SmartbchContractApi* | [**smart_bch_contract_call**](docs/SmartbchContractApi.md#smart_bch_contract_call) | **POST** /smartbch/contract/call | Call a SmartBch contract function
*SmartbchContractApi* | [**smart_bch_contract_create**](docs/SmartbchContractApi.md#smart_bch_contract_create) | **POST** /smartbch/contract/create | Create a SmartBch contractId
*SmartbchContractApi* | [**smart_bch_contract_deploy**](docs/SmartbchContractApi.md#smart_bch_contract_deploy) | **POST** /smartbch/contract/deploy | Request to deploy a SmartBch contract
*SmartbchContractApi* | [**smart_bch_contract_estimate_gas**](docs/SmartbchContractApi.md#smart_bch_contract_estimate_gas) | **POST** /smartbch/contract/estimate_gas | Estimate the gas for a contract interaction function given the arguments
*SmartbchContractApi* | [**smart_bch_contract_info**](docs/SmartbchContractApi.md#smart_bch_contract_info) | **POST** /smartbch/contract/info | Get information about a SmartBch contract from the contractId
*SmartbchSep20Api* | [**smart_bch_sep20_all_balances**](docs/SmartbchSep20Api.md#smart_bch_sep20_all_balances) | **POST** /smartbch/sep20/all_balances | Get all SmartBch SEP20 balances of the wallet
*SmartbchSep20Api* | [**smart_bch_sep20_balance**](docs/SmartbchSep20Api.md#smart_bch_sep20_balance) | **POST** /smartbch/sep20/balance | Get total SmartBch SEP20 token balance of the wallet
*SmartbchSep20Api* | [**smart_bch_sep20_deposit_address**](docs/SmartbchSep20Api.md#smart_bch_sep20_deposit_address) | **POST** /smartbch/sep20/deposit_address | Get an SmartBch SEP20 deposit address
*SmartbchSep20Api* | [**smart_bch_sep20_deposit_qr**](docs/SmartbchSep20Api.md#smart_bch_sep20_deposit_qr) | **POST** /smartbch/sep20/deposit_qr | Get an SmartBch SEP20 receiving address as a qrcode
*SmartbchSep20Api* | [**smart_bch_sep20_genesis**](docs/SmartbchSep20Api.md#smart_bch_sep20_genesis) | **POST** /smartbch/sep20/genesis | Get created tokenId back and new SmartBch SEP20 token balance of the wallet
*SmartbchSep20Api* | [**smart_bch_sep20_mint**](docs/SmartbchSep20Api.md#smart_bch_sep20_mint) | **POST** /smartbch/sep20/mint | Get created tokenId back and new SmartBch SEP20 token balance of the wallet
*SmartbchSep20Api* | [**smart_bch_sep20_send**](docs/SmartbchSep20Api.md#smart_bch_sep20_send) | **POST** /smartbch/sep20/send | Send some SmartBch SEP20 token amount to a given address
*SmartbchSep20Api* | [**smart_bch_sep20_send_max**](docs/SmartbchSep20Api.md#smart_bch_sep20_send_max) | **POST** /smartbch/sep20/send_max | Send all available SmartBch SEP20 token funds to a given address
*SmartbchSep20Api* | [**smart_bch_sep20_token_info**](docs/SmartbchSep20Api.md#smart_bch_sep20_token_info) | **POST** /smartbch/sep20/token_info | Get information about the SmartBch SEP20 token
*SmartbchWalletApi* | [**smartbch_balance**](docs/SmartbchWalletApi.md#smartbch_balance) | **POST** /smartbch/wallet/balance | Get total balance for wallet
*SmartbchWalletApi* | [**smartbch_create_wallet**](docs/SmartbchWalletApi.md#smartbch_create_wallet) | **POST** /smartbch/wallet/create | create a new wallet
*SmartbchWalletApi* | [**smartbch_deposit_address**](docs/SmartbchWalletApi.md#smartbch_deposit_address) | **POST** /smartbch/wallet/deposit_address | Get a deposit address
*SmartbchWalletApi* | [**smartbch_deposit_qr**](docs/SmartbchWalletApi.md#smartbch_deposit_qr) | **POST** /smartbch/wallet/deposit_qr | Get receiving cash address as a qrcode
*SmartbchWalletApi* | [**smartbch_max_amount_to_send**](docs/SmartbchWalletApi.md#smartbch_max_amount_to_send) | **POST** /smartbch/wallet/max_amount_to_send | Get maximum spendable amount
*SmartbchWalletApi* | [**smartbch_send**](docs/SmartbchWalletApi.md#smartbch_send) | **POST** /smartbch/wallet/send | Send some amount to a given address
*SmartbchWalletApi* | [**smartbch_send_max**](docs/SmartbchWalletApi.md#smartbch_send_max) | **POST** /smartbch/wallet/send_max | Send all available funds to a given address
*SmartbchWalletApi* | [**smartbch_signed_message_sign**](docs/SmartbchWalletApi.md#smartbch_signed_message_sign) | **POST** /smartbch/wallet/signed/sign | Returns the message signature
*SmartbchWalletApi* | [**smartbch_signed_message_verify**](docs/SmartbchWalletApi.md#smartbch_signed_message_verify) | **POST** /smartbch/wallet/signed/verify | Returns a boolean indicating whether message was valid for a given address
*UtilApi* | [**convert**](docs/UtilApi.md#convert) | **POST** /util/convert | convert between units
*UtilApi* | [**get_addrs_by_xpub_key**](docs/UtilApi.md#get_addrs_by_xpub_key) | **POST** /util/get_addrs_by_xpubkey | Derive heristic determined addresses from an extended public key, per BIP32
*UtilApi* | [**get_xpub_key_info**](docs/UtilApi.md#get_xpub_key_info) | **POST** /util/get_xpubkey_info | Decode information about an extended public key, per BIP32
*WalletApi* | [**balance**](docs/WalletApi.md#balance) | **POST** /wallet/balance | Get total balance for wallet
*WalletApi* | [**create_wallet**](docs/WalletApi.md#create_wallet) | **POST** /wallet/create | create a new wallet
*WalletApi* | [**deposit_address**](docs/WalletApi.md#deposit_address) | **POST** /wallet/deposit_address | Get a deposit address in cash address format
*WalletApi* | [**deposit_qr**](docs/WalletApi.md#deposit_qr) | **POST** /wallet/deposit_qr | Get receiving cash address as a qrcode
*WalletApi* | [**encode_transaction**](docs/WalletApi.md#encode_transaction) | **POST** /wallet/encode_transaction | Encode and sign a transaction given a list of sendRequests, options and estimate fees
*WalletApi* | [**get_all_nft_token_balances**](docs/WalletApi.md#get_all_nft_token_balances) | **POST** /wallet/get_all_nft_token_balances | Get non-fungible token balance
*WalletApi* | [**get_all_token_balances**](docs/WalletApi.md#get_all_token_balances) | **POST** /wallet/get_all_token_balances | Get non-fungible token balance
*WalletApi* | [**get_history**](docs/WalletApi.md#get_history) | **POST** /wallet/get_history | Get a simplified list of transactions related to a wallet
*WalletApi* | [**get_nft_token_balance**](docs/WalletApi.md#get_nft_token_balance) | **POST** /wallet/get_nft_token_balance | Get non-fungible token balance
*WalletApi* | [**get_token_balance**](docs/WalletApi.md#get_token_balance) | **POST** /wallet/get_token_balance | Get fungible token balance
*WalletApi* | [**get_token_utxos**](docs/WalletApi.md#get_token_utxos) | **POST** /wallet/get_token_utxos | Get token utxos
*WalletApi* | [**info**](docs/WalletApi.md#info) | **POST** /wallet/info | Get information about a wallet
*WalletApi* | [**max_amount_to_send**](docs/WalletApi.md#max_amount_to_send) | **POST** /wallet/max_amount_to_send | Get maximum spendable amount
*WalletApi* | [**named_exists**](docs/WalletApi.md#named_exists) | **POST** /wallet/named_exists | Check if a named wallet already exists
*WalletApi* | [**replace_named**](docs/WalletApi.md#replace_named) | **POST** /wallet/replace_named | Replace (recover) named wallet with a new walletId. If wallet with a provided name does not exist yet, it will be creted with a &#x60;walletId&#x60; supplied If wallet exists it will be overwritten without exception 
*WalletApi* | [**send**](docs/WalletApi.md#send) | **POST** /wallet/send | Send some amount to a given address
*WalletApi* | [**send_max**](docs/WalletApi.md#send_max) | **POST** /wallet/send_max | Send all available funds to a given address
*WalletApi* | [**submit_transaction**](docs/WalletApi.md#submit_transaction) | **POST** /wallet/submit_transaction | submit an encoded and signed transaction to the network
*WalletApi* | [**token_burn**](docs/WalletApi.md#token_burn) | **POST** /wallet/token_burn | Perform an explicit token burn
*WalletApi* | [**token_deposit_address**](docs/WalletApi.md#token_deposit_address) | **POST** /wallet/token_deposit_address | Get a token aware deposit address in cash address format
*WalletApi* | [**token_deposit_qr**](docs/WalletApi.md#token_deposit_qr) | **POST** /wallet/token_deposit_qr | Get receiving token aware cash address as a qrcode
*WalletApi* | [**token_genesis**](docs/WalletApi.md#token_genesis) | **POST** /wallet/token_genesis | Create new token category
*WalletApi* | [**token_mint**](docs/WalletApi.md#token_mint) | **POST** /wallet/token_mint | Mint new non-fungible tokens
*WalletApi* | [**utxos**](docs/WalletApi.md#utxos) | **POST** /wallet/utxo | Get detailed information about unspent outputs (utxos)
*WalletApi* | [**xpubkeys**](docs/WalletApi.md#xpubkeys) | **POST** /wallet/xpubkeys | A set of xpubkeys and paths for the wallet.
*WalletBcmrApi* | [**bcmr_add_metadata_registry_auth_chain**](docs/WalletBcmrApi.md#bcmr_add_metadata_registry_auth_chain) | **POST** /wallet/bcmr/add_registry_authchain | Add BCMR metadata registry from autchain, returning the built chain
*WalletBcmrApi* | [**bcmr_add_registry**](docs/WalletBcmrApi.md#bcmr_add_registry) | **POST** /wallet/bcmr/add_registry | Add BCMR registry from parameter
*WalletBcmrApi* | [**bcmr_add_registry_from_uri**](docs/WalletBcmrApi.md#bcmr_add_registry_from_uri) | **POST** /wallet/bcmr/add_registry_from_uri | Reset tracked BCMR registries
*WalletBcmrApi* | [**bcmr_build_auth_chain**](docs/WalletBcmrApi.md#bcmr_build_auth_chain) | **POST** /wallet/bcmr/build_authchain | Build a BCMR authchain
*WalletBcmrApi* | [**bcmr_get_registries**](docs/WalletBcmrApi.md#bcmr_get_registries) | **POST** /wallet/bcmr/get_registries | Get tracked BCMR registries
*WalletBcmrApi* | [**bcmr_get_token_info**](docs/WalletBcmrApi.md#bcmr_get_token_info) | **POST** /wallet/bcmr/get_token_info | Get token info
*WalletBcmrApi* | [**bcmr_reset_registries**](docs/WalletBcmrApi.md#bcmr_reset_registries) | **POST** /wallet/bcmr/reset_registries | Reset tracked BCMR registries
*WalletSignedApi* | [**signed_message_sign**](docs/WalletSignedApi.md#signed_message_sign) | **POST** /wallet/signed/sign | Returns the message signature
*WalletSignedApi* | [**signed_message_verify**](docs/WalletSignedApi.md#signed_message_verify) | **POST** /wallet/signed/verify | Returns a boolean indicating whether message was valid for a given address
*WalletSlpApi* | [**nft_child_genesis**](docs/WalletSlpApi.md#nft_child_genesis) | **POST** /wallet/slp/nft_child_genesis | Get created tokenId back and new NFT child token balance of the wallet
*WalletSlpApi* | [**nft_parent_genesis**](docs/WalletSlpApi.md#nft_parent_genesis) | **POST** /wallet/slp/nft_parent_genesis | Get created tokenId back and new NFT token balance of the wallet
*WalletSlpApi* | [**slp_all_balances**](docs/WalletSlpApi.md#slp_all_balances) | **POST** /wallet/slp/all_balances | Get all slp balances of the wallet
*WalletSlpApi* | [**slp_balance**](docs/WalletSlpApi.md#slp_balance) | **POST** /wallet/slp/balance | Get total slp token balance of the wallet
*WalletSlpApi* | [**slp_create_wallet**](docs/WalletSlpApi.md#slp_create_wallet) | **POST** /wallet/slp/create | create a new SLP wallet
*WalletSlpApi* | [**slp_deposit_address**](docs/WalletSlpApi.md#slp_deposit_address) | **POST** /wallet/slp/deposit_address | Get an SLP deposit address in cash address format
*WalletSlpApi* | [**slp_deposit_qr**](docs/WalletSlpApi.md#slp_deposit_qr) | **POST** /wallet/slp/deposit_qr | Get an SLP receiving cash address as a qrcode
*WalletSlpApi* | [**slp_genesis**](docs/WalletSlpApi.md#slp_genesis) | **POST** /wallet/slp/genesis | Get created tokenId back and new slp token balance of the wallet
*WalletSlpApi* | [**slp_mint**](docs/WalletSlpApi.md#slp_mint) | **POST** /wallet/slp/mint | Get created tokenId back and new slp token balance of the wallet
*WalletSlpApi* | [**slp_outpoints**](docs/WalletSlpApi.md#slp_outpoints) | **POST** /wallet/slp/outpoints | Get list of unspent SLP outpoints.
*WalletSlpApi* | [**slp_send**](docs/WalletSlpApi.md#slp_send) | **POST** /wallet/slp/send | Send some SLP token amount to a given cash address
*WalletSlpApi* | [**slp_send_max**](docs/WalletSlpApi.md#slp_send_max) | **POST** /wallet/slp/send_max | Send all available SLP funds to a given address
*WalletSlpApi* | [**slp_token_info**](docs/WalletSlpApi.md#slp_token_info) | **POST** /wallet/slp/token_info | Get information about the token
*WalletSlpApi* | [**slp_utxos**](docs/WalletSlpApi.md#slp_utxos) | **POST** /wallet/slp/utxo | Get detailed information about unspent SLP outputs (utxos)
*WalletUtilApi* | [**util_decode_transaction**](docs/WalletUtilApi.md#util_decode_transaction) | **POST** /wallet/util/decode_transaction | Decode a bitcoin transaction. Accepts both transaction hash or raw transaction in hex format.
*WalletUtilApi* | [**util_get_raw_transaction**](docs/WalletUtilApi.md#util_get_raw_transaction) | **POST** /wallet/util/get_raw_transaction | Get bitcoin raw transaction
*WebhookApi* | [**watch_address**](docs/WebhookApi.md#watch_address) | **POST** /webhook/watch_address | Create a webhook to watch cashaddress balance and transactions. 


## Documentation For Models

 - [AuthChainElement](docs/AuthChainElement.md)
 - [BalanceRequest](docs/BalanceRequest.md)
 - [BalanceResponse](docs/BalanceResponse.md)
 - [CashscriptReceipt](docs/CashscriptReceipt.md)
 - [Contract](docs/Contract.md)
 - [ContractFnRequest](docs/ContractFnRequest.md)
 - [ContractFnResponse](docs/ContractFnResponse.md)
 - [ContractInfoRequest](docs/ContractInfoRequest.md)
 - [ContractInfoResponse](docs/ContractInfoResponse.md)
 - [ContractRequest](docs/ContractRequest.md)
 - [ContractResponse](docs/ContractResponse.md)
 - [ConvertRequest](docs/ConvertRequest.md)
 - [CreateSignedMessageRequest](docs/CreateSignedMessageRequest.md)
 - [DepositAddressResponse](docs/DepositAddressResponse.md)
 - [ElectrumRawTransaction](docs/ElectrumRawTransaction.md)
 - [ElectrumRawTransactionScriptPubKey](docs/ElectrumRawTransactionScriptPubKey.md)
 - [ElectrumRawTransactionScriptSig](docs/ElectrumRawTransactionScriptSig.md)
 - [ElectrumRawTransactionVin](docs/ElectrumRawTransactionVin.md)
 - [ElectrumRawTransactionVout](docs/ElectrumRawTransactionVout.md)
 - [EncodeTransactionRequest](docs/EncodeTransactionRequest.md)
 - [EncodeTransactionResponse](docs/EncodeTransactionResponse.md)
 - [Error](docs/Error.md)
 - [EscrowContract](docs/EscrowContract.md)
 - [EscrowFnRequest](docs/EscrowFnRequest.md)
 - [EscrowInfoRequest](docs/EscrowInfoRequest.md)
 - [EscrowInfoResponse](docs/EscrowInfoResponse.md)
 - [EscrowRequest](docs/EscrowRequest.md)
 - [EscrowResponse](docs/EscrowResponse.md)
 - [GetAddressesResponse](docs/GetAddressesResponse.md)
 - [GetAddrsByXpubKeyRequest](docs/GetAddrsByXpubKeyRequest.md)
 - [GetTestnetBchRequest](docs/GetTestnetBchRequest.md)
 - [GetTestnetBchResponse](docs/GetTestnetBchResponse.md)
 - [GetTestnetSbchRequest](docs/GetTestnetSbchRequest.md)
 - [GetTestnetSbchResponse](docs/GetTestnetSbchResponse.md)
 - [GetTestnetSep20Request](docs/GetTestnetSep20Request.md)
 - [GetTestnetSep20Response](docs/GetTestnetSep20Response.md)
 - [GetTestnetSlpRequest](docs/GetTestnetSlpRequest.md)
 - [GetTestnetSlpResponse](docs/GetTestnetSlpResponse.md)
 - [GetXpubKeyInfoRequest](docs/GetXpubKeyInfoRequest.md)
 - [GetXpubKeyInfoResponse](docs/GetXpubKeyInfoResponse.md)
 - [HistoryRequest](docs/HistoryRequest.md)
 - [HistoryResponse](docs/HistoryResponse.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [InlineObject4](docs/InlineObject4.md)
 - [MaxAmountToSendRequest](docs/MaxAmountToSendRequest.md)
 - [MineRequest](docs/MineRequest.md)
 - [NetworkEnum](docs/NetworkEnum.md)
 - [OpReturnData](docs/OpReturnData.md)
 - [ScalableVectorGraphic](docs/ScalableVectorGraphic.md)
 - [SendMaxRequest](docs/SendMaxRequest.md)
 - [SendMaxResponse](docs/SendMaxResponse.md)
 - [SendRequest](docs/SendRequest.md)
 - [SendRequestItem](docs/SendRequestItem.md)
 - [SendRequestItemAnyOf](docs/SendRequestItemAnyOf.md)
 - [SendRequestOptions](docs/SendRequestOptions.md)
 - [SendResponse](docs/SendResponse.md)
 - [SerializedWallet](docs/SerializedWallet.md)
 - [SignedMessageResponse](docs/SignedMessageResponse.md)
 - [SignedMessageResponseDetails](docs/SignedMessageResponseDetails.md)
 - [SignedMessageResponseRaw](docs/SignedMessageResponseRaw.md)
 - [SlpBalanceRequest](docs/SlpBalanceRequest.md)
 - [SlpBalanceResponse](docs/SlpBalanceResponse.md)
 - [SlpDepositAddressResponse](docs/SlpDepositAddressResponse.md)
 - [SlpGenesisRequest](docs/SlpGenesisRequest.md)
 - [SlpGenesisResponse](docs/SlpGenesisResponse.md)
 - [SlpMintRequest](docs/SlpMintRequest.md)
 - [SlpMintResponse](docs/SlpMintResponse.md)
 - [SlpOutpointsResponse](docs/SlpOutpointsResponse.md)
 - [SlpSendMaxRequest](docs/SlpSendMaxRequest.md)
 - [SlpSendRequest](docs/SlpSendRequest.md)
 - [SlpSendRequestItem](docs/SlpSendRequestItem.md)
 - [SlpSendRequestOptions](docs/SlpSendRequestOptions.md)
 - [SlpSendResponse](docs/SlpSendResponse.md)
 - [SlpTokenInfoRequest](docs/SlpTokenInfoRequest.md)
 - [SlpTokenInfoResponse](docs/SlpTokenInfoResponse.md)
 - [SlpUtxo](docs/SlpUtxo.md)
 - [SlpUtxoResponse](docs/SlpUtxoResponse.md)
 - [SmartBchContractDeployRequest](docs/SmartBchContractDeployRequest.md)
 - [SmartBchContractDeployResponse](docs/SmartBchContractDeployResponse.md)
 - [SmartBchContractEstimateGasRequest](docs/SmartBchContractEstimateGasRequest.md)
 - [SmartBchContractEstimateGasResponse](docs/SmartBchContractEstimateGasResponse.md)
 - [SmartBchContractFnCallRequest](docs/SmartBchContractFnCallRequest.md)
 - [SmartBchContractFnCallResponse](docs/SmartBchContractFnCallResponse.md)
 - [SmartBchContractInfoRequest](docs/SmartBchContractInfoRequest.md)
 - [SmartBchContractInfoResponse](docs/SmartBchContractInfoResponse.md)
 - [SmartBchContractRequest](docs/SmartBchContractRequest.md)
 - [SmartBchContractResponse](docs/SmartBchContractResponse.md)
 - [SmartBchDepositAddressResponse](docs/SmartBchDepositAddressResponse.md)
 - [SmartBchMaxAmountToSendRequest](docs/SmartBchMaxAmountToSendRequest.md)
 - [SmartBchOverrides](docs/SmartBchOverrides.md)
 - [SmartBchSendMaxRequest](docs/SmartBchSendMaxRequest.md)
 - [SmartBchSendRequest](docs/SmartBchSendRequest.md)
 - [SmartBchSendRequestItem](docs/SmartBchSendRequestItem.md)
 - [SmartBchSendRequestItemAnyOf](docs/SmartBchSendRequestItemAnyOf.md)
 - [SmartBchSendRequestOptions](docs/SmartBchSendRequestOptions.md)
 - [SmartBchSendResponseItem](docs/SmartBchSendResponseItem.md)
 - [SmartBchSep20AllBalancesRequest](docs/SmartBchSep20AllBalancesRequest.md)
 - [SmartBchSep20BalanceRequest](docs/SmartBchSep20BalanceRequest.md)
 - [SmartBchSep20BalanceResponse](docs/SmartBchSep20BalanceResponse.md)
 - [SmartBchSep20GenesisRequest](docs/SmartBchSep20GenesisRequest.md)
 - [SmartBchSep20GenesisResponse](docs/SmartBchSep20GenesisResponse.md)
 - [SmartBchSep20MintRequest](docs/SmartBchSep20MintRequest.md)
 - [SmartBchSep20MintResponse](docs/SmartBchSep20MintResponse.md)
 - [SmartBchSep20SendMaxRequest](docs/SmartBchSep20SendMaxRequest.md)
 - [SmartBchSep20SendRequest](docs/SmartBchSep20SendRequest.md)
 - [SmartBchSep20SendRequestItem](docs/SmartBchSep20SendRequestItem.md)
 - [SmartBchSep20TokenInfoRequest](docs/SmartBchSep20TokenInfoRequest.md)
 - [SmartBchSep20TokenInfoResponse](docs/SmartBchSep20TokenInfoResponse.md)
 - [SmartBchTransactionReceipt](docs/SmartBchTransactionReceipt.md)
 - [SubmitTransactionRequest](docs/SubmitTransactionRequest.md)
 - [SubmitTransactionResponse](docs/SubmitTransactionResponse.md)
 - [TokenBurnRequest](docs/TokenBurnRequest.md)
 - [TokenGenesisRequest](docs/TokenGenesisRequest.md)
 - [TokenMintRequest](docs/TokenMintRequest.md)
 - [TokenMintRequestRequests](docs/TokenMintRequestRequests.md)
 - [TokenSendRequest](docs/TokenSendRequest.md)
 - [TransactionHistoryItem](docs/TransactionHistoryItem.md)
 - [UnitType](docs/UnitType.md)
 - [UtilDecodeTransactionRequest](docs/UtilDecodeTransactionRequest.md)
 - [Utxo](docs/Utxo.md)
 - [UtxoToken](docs/UtxoToken.md)
 - [VerifySignedMessageRequest](docs/VerifySignedMessageRequest.md)
 - [VerifySignedMessageResponse](docs/VerifySignedMessageResponse.md)
 - [VerifySignedMessageResponseDetails](docs/VerifySignedMessageResponseDetails.md)
 - [WalletInfo](docs/WalletInfo.md)
 - [WalletMnemonic](docs/WalletMnemonic.md)
 - [WalletNamedExistsRequest](docs/WalletNamedExistsRequest.md)
 - [WalletReplaceNamedRequest](docs/WalletReplaceNamedRequest.md)
 - [WalletRequest](docs/WalletRequest.md)
 - [WalletResponse](docs/WalletResponse.md)
 - [WalletType](docs/WalletType.md)
 - [WatchAddressRequest](docs/WatchAddressRequest.md)
 - [WatchAddressResponse](docs/WatchAddressResponse.md)
 - [Wif](docs/Wif.md)
 - [XPubKey](docs/XPubKey.md)
 - [XPubKeyRequest](docs/XPubKeyRequest.md)
 - [XPubKeyResponse](docs/XPubKeyResponse.md)
 - [ZeroBalanceResponse](docs/ZeroBalanceResponse.md)


## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication


## Author

hello@mainnet.cash


