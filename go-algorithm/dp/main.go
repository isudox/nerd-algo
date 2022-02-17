package main

import (
	"encoding/json"
	"fmt"
	"time"
)

type Param struct {
	Num  *int
	Name *string
	Time *time.Time
}

func main() {
	//param := &Param{
	//	Num:  0,
	//	Name: "A",
	//}
	//output, _ := json.Marshal(param)
	//fmt.Printf("param: %v\n", string(output))
	input := "{\"Num\":0,\"Name\":\"A\"}"
	obj := &Param{}
	json.Unmarshal([]byte(input), obj)
	fmt.Printf("param: %v, %v, %v\n", obj.Num, obj.Name, obj.Time)

	// otp := otp{}

	// smsOTP := &sms{
	//  otp: otp,
	// }

	// smsOTP.genAndSendOTP(smsOTP, 4)

	// emailOTP := &email{
	//  otp: otp,
	// }
	// emailOTP.genAndSendOTP(emailOTP, 4)
	// fmt.Scanln()
	smsOTP := &sms{}
	o := otp{
		iOtp: smsOTP,
	}
	o.genAndSendOTP(4)

	fmt.Println("")
	emailOTP := &email{}
	o = otp{
		iOtp: emailOTP,
	}
	o.genAndSendOTP(4)
	a := map[string]otp{
		"a": {iOtp: nil},
	}
	if b, ok := a["b"]; !ok {
		fmt.Println("not")
	} else {
		fmt.Println(b)
	}
}
