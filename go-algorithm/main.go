package main

import "encoding/json"

func main() {
	body := "{\"item_out_order_no\":\"\",\"need_fund_archive\":\"false\",\"payee_id\":\"6953180508134621484\",\"payer_id\":\"4432837368096685\",\"risk_info\":\"流水发生\\u003e0\",\"settle_info\":\"[]\",\"shop_id\":\"94956\"}"
	ext := map[string]interface{}{}
	if err := json.Unmarshal([]byte(body), &ext); err != nil {
		println("err: " + err.Error())
	}
	println("data:" + ext["risk_info"].(string))
}
