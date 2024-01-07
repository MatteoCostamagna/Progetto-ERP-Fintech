package internal

import "time"

type Capacity struct{
	Timestamp         int       `json:"timestamp"`
	EntryNo           int       `json:"entry_no"`
	PostingDate       time.Time `json:"posting_date"`
	Type              int       `json:"type"`
	Description       string    `json:"description"`
	WorkCenterNo      string    `json:"work_center_no_"`
	Quantity          int       `json:"quantity"`
	SetupTime         int       `json:"setup_time"`
	RunTime           int       `json:"run_time"`
	StopTime          int       `json:"stop_time"`
	InvoicedQuantity  int       `json:"invoiced_quantity"`
	OutputQuantity    int       `json:"output_quantity"`
	ScrapQuantity     int       `json:"scrap_quantity"`
}