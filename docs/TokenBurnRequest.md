# TokenBurnRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The walletId to make a request to. | 
**requests** | [**list[TokenBurnItem]**](TokenBurnItem.md) | One or more burn requests. Requests can span multiple categories, all burned in a single transaction sharing one OP_RETURN. | 
**message** | **str** | optional message to include in OP_RETURN | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


