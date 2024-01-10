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
	
	
	wg.Add(1)
	go func () {
		if len(finTsCapacity) == 0 {
			go pkg.Get_request_all[internal.Capacity]("", finChanCapacityData)
		}else {
			
			erpChanTsCapacity := make(chan []pkg.Timestamp)
			
			go pkg.Get_request_ts("",erpChanTsCapacity)
			
			erpTsCapacity := <-erpChanTsCapacity

			updatedTsCapacity, valueToDeleteCapacity := pkg.New_values(erpTsCapacity,finTsCapacity)

			err := pkg.Delete_request("",valueToDeleteCapacity)
			if err != nil {
				fmt.Println(err)
			}
			go pkg.Get_request_capacity_erp(finChanCapacityData,updatedTsCapacity)
		}

		wg.Done()
		}()
	
	wg.Add(1)
	go func() {
		if len(finTsItem) == 0 {
			go pkg.Get_request_all[internal.Item]("", finChanItemData)
		} else {
			erpChanTsItem := make(chan []pkg.Timestamp)

			go pkg.Get_request_ts("",erpChanTsItem)

			erpTsItem :=<-erpChanTsItem

			updatedTsItem,valueToDeleteItem := pkg.New_values(erpTsItem,finTsItem)

			err := pkg.Delete_request("",valueToDeleteItem)
			if err != nil {
				fmt.Println(err)
			}
			go pkg.Get_request_item_erp(finChanItemData,updatedTsItem)
		}
		wg.Done()
	}()
	itemData := <-finChanItemData
	capacityData := <-finChanCapacityData
	
	wg.Add(1)
	go func() {
		res := pkg.Post_request[internal.Item]("", itemData)
		fmt.Println(res)
		}()
	go func() {
		res := pkg.Post_request[internal.Capacity]("",capacityData)
		fmt.Println(res)
	}()
	wg.Wait()
	fmt.Println("Process Completed")
}
