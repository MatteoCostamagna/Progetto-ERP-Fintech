package pkg

import (
	"encoding/json"
	"io"
	"log"
	"net/http"
)

/*
Get request for the timestamp
*/
func get_request_ts(url string , c chan []Timestamp) error {
	
	resp,err := http.Get(url)

	if err != nil {
		log.Fatalln(err)
	}
	
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)

	if err != nil {
		log.Fatalln(err)
	}

	var timestamp []Timestamp
	err = json.Unmarshal(body,&timestamp)

	if err != nil {
		log.Fatalln(err)
	}

	c <- timestamp

	return nil
}

func get_request_erp(url string)  {
	
}