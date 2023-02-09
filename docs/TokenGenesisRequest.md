# TokenGenesisRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The walletId to make a request to. | 
**amount** | **float** | amount of *fungible* tokens to create | [optional] 
**capability** | **str** | Capability of the new NFT | [optional] 
**commitment** | **str** | Token commitment message, hexadecimal encoded, 40 bytes max length | [optional] 
**cashaddr** | **str** | Cashaddress to send tokens to | [optional] 
**value** | **float** | Satoshi value to send alongside with tokens | [optional] [default to 1000]
**send_requests** | [**AnyOfSendRequestItemarrayTokenSendRequestOpReturnData**](AnyOfSendRequestItemarrayTokenSendRequestOpReturnData.md) | Single or an array of extra send requests (OP_RETURN, value transfer, etc.) to include in genesis transaction. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


