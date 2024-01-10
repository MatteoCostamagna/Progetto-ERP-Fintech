package pkg

import (
	"bytes"
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
func Get_request_ts(url string, c chan []Timestamp) error {

	resp, err := http.Get(url)

	if err != nil {
		log.Fatalln(err)
	}

	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)

	if err != nil {
		log.Fatalln(err)
	}

	var timestamp []Timestamp
	
	err = json.Unmarshal(body, &timestamp)

	if err != nil {
        var timestamps []any
		err = json.Unmarshal(body,&timestamps) 
		
		if err != nil{
			log.Fatalln(err)
		}


	}

	c <- timestamp

	return nil
}

func Get_request_capacity_erp(c chan []internal.Capacity, timestamp []uint64) {
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

	if err != nil {
		log.Fatal(err)
	}

	c <- capacity

}

func Get_request_item_erp(c chan []internal.Item, timestamp []uint64) {
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

	if err != nil {
		log.Fatal(err)
	}

	c <- item
}

func Post_request[T internal.Capacity | internal.Item](URL string, data []T) any {

	jsonData, err := json.Marshal(data)

	if err != nil {
		log.Fatalln(err)
	}

	res, err := http.Post(URL, "application/json", bytes.NewBuffer(jsonData))

	if err != nil {
		log.Fatal(err)
	}

	defer res.Body.Close()

	if res.StatusCode != http.StatusCreated {
		fmt.Printf("Error on code received: %d", res.StatusCode)
	}
	return res.StatusCode
}

func Delete_request(URL string, timestamps []uint64) error {

	u, err := url.Parse(URL)

	if err != nil {
		log.Fatal(err)
	}

	q := u.Query()

	for _, ts := range timestamps {
		q.Add("timestamp", fmt.Sprint(ts))
	}

	u.RawQuery = q.Encode()

	req, err := http.NewRequest("DELETE", u.String(), nil)

	if err != nil {
		return fmt.Errorf("failed to create DELETE request: %v", err)
	}

	client := http.DefaultClient

	res, err := client.Do(req)

	if err != nil {
		return fmt.Errorf("failed to perform DELETE request: %v", err)
	}
	defer res.Body.Close()

	if res.StatusCode != http.StatusOK {
		return fmt.Errorf("unexpected status code: %d", res.StatusCode)
	}

	return nil
}

func Get_request_all[T internal.Capacity | internal.Item](URL string, c chan []T) {

	res, err := http.Get(URL)

	if err != nil {
		fmt.Println("Error making get Request: ", err)
		return
	}
	defer res.Body.Close()

	body, err := io.ReadAll(res.Body)

	if err != nil {
		fmt.Println("Error reading body: ", err)
		return
	}

	var data []T

	err = json.Unmarshal(body, &data)
	if err != nil {
		log.Fatalln("json unmarshal: ",err)
	}

	c <- data
}
