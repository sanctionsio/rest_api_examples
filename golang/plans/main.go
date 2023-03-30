package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strings"
)

const (
	hostname    = "api.sanctions.io"
	bearerToken = "12345678-12AF-12aF-12aF-1234567890aF"
	apiVersion  = "2.1"
)

func main() {
	data, err := invokePlans()
	if err != nil {
		log.Fatal(err)
	} else {
		results := data["results"].([]interface{})
		names := make([]string, len(results))
		for i, result := range results {
			names[i] = result.(map[string]interface{})["plan_name"].(string)
		}
		log.Printf("Plans found: %s", strings.Join(names, ", "))
	}
}

// Example showing how to invoke the /plans function in the sanctions.io REST api
func invokePlans() (map[string]interface{}, error) {
	client := &http.Client{}
	req, err := http.NewRequest("GET", fmt.Sprintf("https://%s/plans", hostname), nil)
	if err != nil {
		return nil, err
	}

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
