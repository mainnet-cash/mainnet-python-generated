# SmartBchContractFnCallResponse

Contract function evaluation response. A constant function (non state changing, also does not cost gas) evaluates to a `result` field A state changing function will generate a transaction and `txId` and `receipt` fields will be filled 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_id** | **str** | serialized contract | [optional] 
**result** | **object** | contract function evaluation result. Can be of any type. | [optional] 
**tx_id** | **str** | The hash of a transaction | [optional] 
**receipt** | [**SmartBchTransactionReceipt**](SmartBchTransactionReceipt.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


