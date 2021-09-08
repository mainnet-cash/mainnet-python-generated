# SmartBchContractEstimateGasRequest

Estimate the gas for a contract function interaction. For a state-changing methods `walletId` is required.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | Serialized wallet | [optional] 
**contract_id** | **str** | serialized contract | 
**function** | **str** | Function to call on the SmartBch contract. | 
**arguments** | **list[object]** | Arguments for the contract function call. Binary and BigNumber data should be passed as hexadecimal.  | [optional] 
**overrides** | [**SmartBchOverrides**](SmartBchOverrides.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


