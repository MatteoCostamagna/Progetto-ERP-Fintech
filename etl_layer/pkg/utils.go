package pkg


type Timestamp struct{
	Timestamp uint64 `json:"timestamp"`
}

/*
@param array of timestamp
Function to retrive value from an array of Timestamp
 write an array of values to a channel 
*/
func get_values(array[]Timestamp,c chan []uint64) {
	var array_ts_value []uint64
	for _, v := range array {
		array_ts_value = append(array_ts_value, v.Timestamp)
	}
	c <- array_ts_value
}


/**
Function that find the difference value in a array
*/
func New_values(ts_erp[]Timestamp,ts_fin[]Timestamp) ([]uint64,[]uint64) {
	res_erp := make(chan []uint64)
	res_fin := make(chan []uint64)
	go get_values(ts_erp,res_erp)
	go get_values(ts_fin,res_fin)
	fin_value := <-res_fin
	erp_value := <-res_erp
	updated_ts := []uint64{}
	missing_value := []uint64{}
	for idx, val := range erp_value{
		if len(fin_value) > 0 { 
			if val != fin_value[idx]{
				updated_ts = append(updated_ts, val)
				missing_value = append(missing_value, fin_value[idx])
			}
		}else {
			updated_ts = append(updated_ts, val)
		}
	}
	return updated_ts, missing_value
}

