package internal


type Capacity struct {
	Timestamp        int       `json:"timestamp"`
	EntryNo          int       `json:"entry_no"`
	PostingDate      MyTime `json:"posting_date"`
	Type             int       `json:"type"`
	Description      string    `json:"description"`
	WorkCenterNo     string    `json:"work_center_no"`
	Quantity         float32      `json:"quantity"`
	SetupTime        float32       `json:"setup_time"`
	RunTime          float32       `json:"run_time"`
	StopTime         float32       `json:"stop_time"`
	InvoicedQuantity float32       `json:"invoiced_quantity"`
	OutputQuantity   float32       `json:"output_quantity"`
	ScrapQuantity    float32       `json:"scrap_quantity"`
}
