# SlpGenesisRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | ID that is returned in &#x60;wallet&#x60; field of /wallet call  | 
**name** | **str** |  | 
**ticker** | **str** | Token ticker | 
**initial_amount** | **str** | Value is represented as a string to avoid precision loss | 
**decimals** | **float** | Indicates that 1 token is divisible into 10^decimals base units | 
**document_url** | **str** |  | [optional] 
**document_hash** | **str** | Document hash of the token. Empty or 64 character long hex string. | [optional] 
**end_baton** | **bool** | Indicates if token should not be &#39;mintable&#39;, e.g. total circulation amount increased | [optional] 
**type** | **float** | Token type. 0x01 Type1, 0x81 NFT Parent, 0x41 NFT Child | [optional] 
**token_receiver_slp_addr** | **str** |  | [optional] 
**baton_receiver_slp_addr** | **str** |  | [optional] 
**parent_token_id** | **str** | Identifier of the NFT parent token | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


