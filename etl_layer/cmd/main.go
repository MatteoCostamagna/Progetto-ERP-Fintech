package main

import (
	"etl-layer/internal"
	"etl-layer/pkg"
	"fmt"
	"os"
	"sync"
)

var wg = sync.WaitGroup{}

func main() {

	finChanCapacityTs := make(chan []pkg.Timestamp)
	finChanItemTs := make(chan []pkg.Timestamp)

	fmt.Println("I start the request for the ts of fin")
	go pkg.Get_request_ts("http://localhost:90/timestamp/capacity_ledger_entry", finChanCapacityTs)
	go pkg.Get_request_ts("http://localhost:90/timestamp/item_ledger_entry", finChanItemTs)

	fmt.Println("1")
	finTsCapacity := <-finChanCapacityTs
	finTsItem := <-finChanItemTs
	fmt.Println("2")
	finChanCapacityData := make(chan []internal.Capacity)
	finChanItemData := make(chan []internal.Item)
	
	
	wg.Add(1)
	go func () {
		fmt.Println("3")
		if len(finTsCapacity) == 0 {
			go pkg.Get_request_all[internal.Capacity]("http://localhost:80/capacity", finChanCapacityData)
		}else {
			erpChanTsCapacity := make(chan []pkg.Timestamp)
			
			go pkg.Get_request_ts("http://localhost:80/timestamp/capacity",erpChanTsCapacity)
			
			erpTsCapacity := <-erpChanTsCapacity

			updatedTsCapacity, valueToDeleteCapacity := pkg.New_values(erpTsCapacity,finTsCapacity)

			err := pkg.Delete_request("http://localhost:90/delete/capacity_ledger_entry/",valueToDeleteCapacity)
			if err != nil {
				fmt.Println(err)
			}
			go pkg.Get_request_capacity_erp(finChanCapacityData,updatedTsCapacity)
		}

		wg.Done()
		}()
	
	wg.Add(1)
	go func() {
		fmt.Println("4")
		if len(finTsItem) == 0 {
			go pkg.Get_request_all[internal.Item]("http://localhost:80/item", finChanItemData)
		} else {
			erpChanTsItem := make(chan []pkg.Timestamp)

			go pkg.Get_request_ts("http://localhost:80/timestamp/item",erpChanTsItem)

			erpTsItem :=<-erpChanTsItem

			updatedTsItem,valueToDeleteItem := pkg.New_values(erpTsItem,finTsItem)

			err := pkg.Delete_request("http://localhost:90/delete/item_ledger_entry/",valueToDeleteItem)
			if err != nil {
				fmt.Println(err)
			}
			go pkg.Get_request_item_erp(finChanItemData,updatedTsItem)
		}
		wg.Done()
	}()
	itemData := <-finChanItemData
	capacityData := <-finChanCapacityData
	
	if (len(itemData)+ len(capacityData)) == 0 {
		fmt.Println("There are no new value is itemData and capacityData")
		os.Exit(0)
	}
	
	fmt.Println("5")
	fmt.Println("ITEM: ",itemData)
	fmt.Println("CAPACITY: ",capacityData)
	wg.Add(1)
	go func() {
		fmt.Println("6")
		res := pkg.Post_request[internal.Item]("http://localhost:90/upload-item-ledger", itemData)
		fmt.Println("Post Item, ", res)
		wg.Done()
		}()
	wg.Add(1)
	go func() {
		fmt.Println("7")
		res := pkg.Post_request[internal.Capacity]("http://localhost:90/upload-capacity-ledger",capacityData)
		fmt.Println("Post Capacity, ",res)
		wg.Done()
	}()
	wg.Wait()
	fmt.Println("Process Completed")
}
