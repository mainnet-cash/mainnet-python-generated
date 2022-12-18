# TokenBurnRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The walletId to make a request to. | 
**token_id** | **str** | Token unique hexadecimal identifier, also the id of the token creation transaction | 
**capability** | **str** | Capability of the new NFT | [optional] 
**commitment** | **str** | Token commitment message, hexadecimal encoded, 40 bytes max length | [optional] 
**amount** | **float** | amount of fungible tokens to burn | [optional] 
**cashaddr** | **str** | address to return token and satoshi change to, default to the sender&#39;s cashaddr | [optional] 
**message** | **str** | optional message to include in OP_RETURN | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


