# TokenGenesisRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The walletId to make a request to. | 
**requests** | [**list[TokenGenesisItem]**](TokenGenesisItem.md) | One or more genesis requests. Each consumes a distinct vout&#x3D;0 input and creates a new token category in the same transaction. | 
**send_requests** | [**AnyOfSendRequestItemarrayTokenSendRequestOpReturnData**](AnyOfSendRequestItemarrayTokenSendRequestOpReturnData.md) | Single or an array of extra send requests (OP_RETURN, value transfer, etc.) to include in genesis transaction. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


