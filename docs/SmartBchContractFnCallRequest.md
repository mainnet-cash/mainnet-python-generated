# SmartBchContractFnCallRequest

Contract function evaluation request. A constant function (non state changing, also does not cost gas) does not require a signer (walletId) A state changing function will generate a transaction and does require a signer (walletId) 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | Serialized wallet | [optional] 
**contract_id** | **str** | serialized contract | 
**function** | **str** | Function to call on the SmartBch contract. | 
**arguments** | **list[object]** | Arguments for the contract function call. Binary and BigNumber data should be passed as hexadecimal.  | [optional] 
**overrides** | [**SmartBchOverrides**](SmartBchOverrides.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


