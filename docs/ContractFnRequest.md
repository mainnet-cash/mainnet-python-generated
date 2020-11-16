# ContractFnRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_id** | **str** | serialized contract  | 
**wallet_id** | **str** | ID that is returned in &#x60;wallet&#x60; field of /wallet call  | 
**action** | **str** | Action for finalization of contract. | 
**get_hex_only** | **bool** | getHexOnly (default:false), if true, will cause only the transaction hex to be returned; if false, the transaction will be sent to the network  | [optional] 
**utxo_ids** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


