package pkg

import (
	"encoding/json"
	"etl-layer/internal"
	"fmt"
	"io"
	"log"
	"net/http"
	"net/url"
)

/*
Get request for the timestamp
*/
func Get_request_ts(url string , c chan []Timestamp) error {
	
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

func Get_request_capacity_erp(c chan[]internal.Capacity, timestamp []uint64)  {
	URL := "http://localhost:80/capacity/"

	u, err := url.Parse(URL)

	if err != nil {
		log.Fatal(err)
	}
	q := u.Query()

	for _, ts := range timestamp {
		q.Add("timestamps", fmt.Sprint(ts))
	}

	u.RawQuery = q.Encode()

	res, err := http.Get(u.String())
	
	if err != nil {
		log.Fatal(err)
	}

	defer res.Body.Close()

	var capacity []internal.Capacity

	err = json.NewDecoder(res.Body).Decode(&capacity)

	if err != nil{
		log.Fatal(err)
	}

	c <- capacity

}

func Get_request_item_erp(c chan[]internal.Item, timestamp[]uint64)  {
	URL := "http://localhost:80/item/"

	u, err := url.Parse(URL)

	if err != nil {
		log.Fatal(err)
	}
	q := u.Query()

	for _, ts := range timestamp {
		q.Add("timestamps", fmt.Sprint(ts))
	}

	u.RawQuery = q.Encode()

	res, err := http.Get(u.String())
	
	if err != nil {
		log.Fatal(err)
	}

	defer res.Body.Close()

	var item []internal.Item

	err = json.NewDecoder(res.Body).Decode(&item)

	if err != nil{
		log.Fatal(err)
	}

	c <- item
}

