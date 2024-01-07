package internal

import "time"

type Item struct{
	Timestamp              uint64     `json:"timestamp"`
	EntryNo                uint     `json:"entry_no"`
	ItemNo                 string  `json:"item_no"`
	PostingDate            time.Time  `json:"posting_date"`
	EntryType              uint     `json:"entry_type"`
	Description            string  `json:"description"`
	LocationCode           string  `json:"location_code"`
	Quantity               float64     `json:"quantity"`
	RemainingQuantity      float64     `json:"remaining_quantity"`
	InvoicedQuantity       float64     `json:"invoiced_quantity"`
	TransactionType        string  `json:"transaction_type"`
	CountryRegionCode      string  `json:"country_region_code"`
	Area                   string  `json:"area"`
	OrderType              uint     `json:"order_type"`
	CompletelyInvoiced     uint     `json:"completely_invoiced"`
	ShippedQtyNotReturned  float64     `json:"shipped_qty_not_returned"`
	ReturnReasonCode       string  `json:"return_reason_code"`
}