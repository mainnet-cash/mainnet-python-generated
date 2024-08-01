# TransactionHistoryItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | [**list[InOutput]**](InOutput.md) |  | [optional] 
**outputs** | [**list[InOutput]**](InOutput.md) |  | [optional] 
**blockheight** | **float** | The blockheight of transaction | [optional] 
**timestamp** | **str** | The timestamp of transaction, undefined if unconfirmed | [optional] 
**hash** | **str** | The hash of the transaction | [optional] 
**size** | **float** | The size of the transaction | [optional] 
**fee** | **float** | Transaction fee | [optional] 
**balance** | **float** | A running balance, in units | [optional] 
**value_change** | **float** | Change of value in the transaction, in units | [optional] 
**token_amount_changes** | [**list[TokenAmountChange]**](TokenAmountChange.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


