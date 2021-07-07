# mainnet
A developer friendly bitcoin cash wallet api

This API is currently in *active* development, breaking changes may
be made prior to official release of version 1.0.0.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.3.20
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
*ContractApi* | [**contract_utxos**](docs/ContractApi.md#contract_utxos) | **POST** /contract/utxos | List specific utxos on any contract
*ContractApi* | [**create_contract**](docs/ContractApi.md#create_contract) | **POST** /contract/create | Create a cashscript contract
*ContractEscrowApi* | [**create_escrow**](docs/ContractEscrowApi.md#create_escrow) | **POST** /contract/escrow/create | Create an escrow contract
*ContractEscrowApi* | [**escrow_fn**](docs/ContractEscrowApi.md#escrow_fn) | **POST** /contract/escrow/call | Finalize an escrow contract
*FaucetApi* | [**get_addresses**](docs/FaucetApi.md#get_addresses) | **POST** /faucet/get_addresses | Get addresses to return back or donate the testnet bch and tokens 
*FaucetApi* | [**get_testnet_bch**](docs/FaucetApi.md#get_testnet_bch) | **POST** /faucet/get_testnet_bch | Get testnet bch 
*FaucetApi* | [**get_testnet_slp**](docs/FaucetApi.md#get_testnet_slp) | **POST** /faucet/get_testnet_slp | Get testnet slp tokens 
*MineApi* | [**mine**](docs/MineApi.md#mine) | **POST** /mine | Mine regtest coins to a specified address
*UtilApi* | [**convert**](docs/UtilApi.md#convert) | **POST** /util/convert | convert between units
*WalletApi* | [**balance**](docs/WalletApi.md#balance) | **POST** /wallet/balance | Get total balance for wallet
*WalletApi* | [**create_wallet**](docs/WalletApi.md#create_wallet) | **POST** /wallet/create | create a new wallet
*WalletApi* | [**deposit_address**](docs/WalletApi.md#deposit_address) | **POST** /wallet/deposit_address | Get a deposit address in cash address format
*WalletApi* | [**deposit_qr**](docs/WalletApi.md#deposit_qr) | **POST** /wallet/deposit_qr | Get receiving cash address as a qrcode
*WalletApi* | [**info**](docs/WalletApi.md#info) | **POST** /wallet/info | Get information about a wallet
*WalletApi* | [**max_amount_to_send**](docs/WalletApi.md#max_amount_to_send) | **POST** /wallet/max_amount_to_send | Get maximum spendable amount
*WalletApi* | [**named_exists**](docs/WalletApi.md#named_exists) | **POST** /wallet/named_exists | Check if a named wallet already exists
*WalletApi* | [**replace_named**](docs/WalletApi.md#replace_named) | **POST** /wallet/replace_named | Replace (recover) named wallet with a new walletId. If wallet with a provided name does not exist yet, it will be creted with a &#x60;walletId&#x60; supplied If wallet exists it will be overwritten without exception 
*WalletApi* | [**send**](docs/WalletApi.md#send) | **POST** /wallet/send | Send some amount to a given address
*WalletApi* | [**send_max**](docs/WalletApi.md#send_max) | **POST** /wallet/send_max | Send all available funds to a given address
*WalletApi* | [**signed_message_sign**](docs/WalletApi.md#signed_message_sign) | **POST** /wallet/signed/sign | Returns the message signature
*WalletApi* | [**signed_message_verify**](docs/WalletApi.md#signed_message_verify) | **POST** /wallet/signed/verify | Returns a boolean indicating whether message was valid for a given address
*WalletApi* | [**utxos**](docs/WalletApi.md#utxos) | **POST** /wallet/utxo | Get detailed information about unspent outputs (utxos)
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
*WebhookApi* | [**watch_address**](docs/WebhookApi.md#watch_address) | **POST** /webhook/watch_address | Create a webhook to watch cashaddress balance and transactions. 


## Documentation For Models

 - [BalanceRequest](docs/BalanceRequest.md)
 - [BalanceResponse](docs/BalanceResponse.md)
 - [CashscriptReceipt](docs/CashscriptReceipt.md)
 - [Contract](docs/Contract.md)
 - [ContractFnRequest](docs/ContractFnRequest.md)
 - [ContractFnResponse](docs/ContractFnResponse.md)
 - [ContractRequest](docs/ContractRequest.md)
 - [ContractResponse](docs/ContractResponse.md)
 - [ConvertRequest](docs/ConvertRequest.md)
 - [CreateSignedMessageRequest](docs/CreateSignedMessageRequest.md)
 - [DepositAddressResponse](docs/DepositAddressResponse.md)
 - [Error](docs/Error.md)
 - [EscrowFnRequest](docs/EscrowFnRequest.md)
 - [EscrowRequest](docs/EscrowRequest.md)
 - [GetAddressesResponse](docs/GetAddressesResponse.md)
 - [GetTestnetBchRequest](docs/GetTestnetBchRequest.md)
 - [GetTestnetBchResponse](docs/GetTestnetBchResponse.md)
 - [GetTestnetSlpRequest](docs/GetTestnetSlpRequest.md)
 - [GetTestnetSlpResponse](docs/GetTestnetSlpResponse.md)
 - [MaxAmountToSendRequest](docs/MaxAmountToSendRequest.md)
 - [MineRequest](docs/MineRequest.md)
 - [NetworkEnum](docs/NetworkEnum.md)
 - [ScalableVectorGraphic](docs/ScalableVectorGraphic.md)
 - [SendMaxRequest](docs/SendMaxRequest.md)
 - [SendMaxResponse](docs/SendMaxResponse.md)
 - [SendRequest](docs/SendRequest.md)
 - [SendRequestItem](docs/SendRequestItem.md)
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
 - [SlpTokenInfoResponseItem](docs/SlpTokenInfoResponseItem.md)
 - [SlpUtxo](docs/SlpUtxo.md)
 - [SlpUtxoResponse](docs/SlpUtxoResponse.md)
 - [UnitType](docs/UnitType.md)
 - [Utxo](docs/Utxo.md)
 - [UtxoResponse](docs/UtxoResponse.md)
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
 - [ZeroBalanceResponse](docs/ZeroBalanceResponse.md)


## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication


## Author

hello@mainnet.cash


