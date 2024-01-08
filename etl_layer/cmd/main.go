package main

import (
	"etl-layer/internal"
	"etl-layer/pkg"
	"fmt"
	"sync"
)

var wg = sync.WaitGroup{}

func main() {

	finChanCapacityTs := make(chan []pkg.Timestamp)
	finChanItemTs := make(chan []pkg.Timestamp)

	go pkg.Get_request_ts("", finChanCapacityTs)
	go pkg.Get_request_ts("", finChanItemTs)

	finTsCapacity := <-finChanCapacityTs
	finTsItem := <-finChanItemTs

	finChanCapacityData := make(chan []internal.Capacity)
	finChanItemData := make(chan []internal.Item)

	go func() {
		if len(finTsCapacity) == 0 {
			go pkg.Get_request_all[internal.Capacity]("", finChanCapacityData)
		}

		wg.Done()
	}()
	wg.Add(1)
	if len(finTsItem) == 0 {
		go pkg.Get_request_all[internal.Item]("", finChanItemData)
	}

	wg.Wait()
	fmt.Println("Process Completed")
}
