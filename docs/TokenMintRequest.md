# TokenMintRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The walletId to make a request to. | 
**token_id** | **str** | Token unique hexadecimal identifier, also the id of the token creation transaction | 
**requests** | [**list[TokenMintRequestRequests]**](TokenMintRequestRequests.md) |  | [optional] 
**deduct_token_amount** | **bool** | if minting token contains fungible amount, deduct from it by amount of minted tokens | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


