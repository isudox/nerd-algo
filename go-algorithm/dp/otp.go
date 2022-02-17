package main

import "fmt"

type iOtp interface {
	genRandomOTP(int) string
	saveOTPCache(string)
	getMessage(string) string
	sendNotification(string) error
	publishMetric()
	abs()
}

type otp struct {
	iOtp iOtp
}

func (o *otp) abs() {
	fmt.Printf("aaaaaa: %s to cache\n", "bbbbbb")
}

func (o *otp) genAndSendOTP(otpLength int) error {
	o.abs()
	otp := o.iOtp.genRandomOTP(otpLength)
	o.iOtp.saveOTPCache(otp)
	message := o.iOtp.getMessage(otp)
	err := o.iOtp.sendNotification(message)
	if err != nil {
		return err
	}
	o.iOtp.publishMetric()
	return nil
}
