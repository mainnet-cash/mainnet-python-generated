# EscrowInfoResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**escrow_contract_id** | **str** | serialized escrow contract  | [optional] 
**script** | **str** | The escrow contract in cashscript syntax  | [optional] 
**parameters** | **list[str]** | Parameters passed when the contract was created | [optional] 
**cashaddr** | **str** |  | [optional] 
**buyer_addr** | **object** | The cashaddress of the buyer | [optional] 
**arbiter_addr** | **object** | The cashaddress of the arbiter | [optional] 
**seller_addr** | **object** | The cashaddress of the seller | [optional] 
**amount** | **float** | Numeric amount to be transferred by the contract in satoshi, amount must be less than 21 BCH. | [optional] 
**nonce** | **float** | A unique number used once for each instance of a contract. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


