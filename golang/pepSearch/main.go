package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

const (
	hostname    = "api.sanctions.io"
	bearerToken = "12345678-12AF-12aF-12aF-1234567890aF"
	apiVersion  = "2.1"
)

func main() {
	data, err := invokePepSearch()
	if err != nil {
		log.Fatal(err)
	} else {
		log.Printf("Counting %v results.", data["count"])
	}
}

// Example showing how to invoke the /pep-search function in the sanctions.io REST api
func invokePepSearch() (map[string]interface{}, error) {
	client := &http.Client{}
	req, err := http.NewRequest("GET", fmt.Sprintf("https://%s/pep-search", hostname), nil)
	if err != nil {
		return nil, err
	}

	query := req.URL.Query()
	query.Add("name", "obama")
	req.URL.RawQuery = query.Encode()

	req.Header.Add("Accept", fmt.Sprintf("application/json; version=%s", apiVersion))
	req.Header.Add("Authorization", fmt.Sprintf("Bearer %s", bearerToken))
	resp, err := client.Do(req)

	if err != nil {
		return nil, err
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}

	var data map[string]interface{}
	err = json.Unmarshal(body, &data)
	if err != nil {
		return nil, err
	} else {
		return data, nil
	}
}
