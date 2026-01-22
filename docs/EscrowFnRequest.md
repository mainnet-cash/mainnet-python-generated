# EscrowFnRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**escrow_contract_id** | **str** | serialized contract  | 
**wallet_id** | **str** | The walletId of the transaction signer.  | 
**function** | **str** | Function to call on the escrow contract. | 
**to** | **str** | Output address for the transaction | [optional] 
**action** | **str** | In addition to &#x60;send&#x60;ing the built transaction, the built transaction hex may be returned (without broadcasting) with &#x60;build&#x60; action. | [optional] 
**utxo_ids** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


