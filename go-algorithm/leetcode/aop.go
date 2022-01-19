package main

import (
	"errors"
	"fmt"
)

// User
type User struct {
	Name string
	Pass string
}

// Auth 验证
func (u *User) Auth() {
	// 实际业务逻辑
	fmt.Printf("register user:%s, use pass:%s\n", u.Name, u.Pass)
}

// UserAdvice
type UserAdvice interface {
	// Before 前置通知
	Before(user *User) error

	// After 后置通知
	After(user *User)
}

// ValidateNameAdvice 用户名验证
type ValidateNameAdvice struct {
}

// ValidatePasswordAdvice 密码验证
type ValidatePasswordAdvice struct {
	MinLength int
	MaxLength int
}

func (ValidateNameAdvice) Before(user *User) error {
	fmt.Println("ValidateNameAdvice before")
	if user.Name == "admin" {
		return errors.New("admin can't be used")
	}
	return nil
}

func (ValidateNameAdvice) After(user *User) {
	fmt.Println("ValidateNameAdvice after")
	fmt.Printf("username:%s validate sucess\n", user.Name)
}

// Before 前置校验
func (advice ValidatePasswordAdvice) Before(user *User) error {
	fmt.Println("ValidatePasswordAdvice before")
	if user.Pass == "123456" {
		return errors.New("pass isn't strong")
	}

	if len(user.Pass) > advice.MaxLength {
		return fmt.Errorf("len of pass must less than:%d", advice.MaxLength)
	}

	if len(user.Pass) < advice.MinLength {
		return fmt.Errorf("len of pass must greater than:%d", advice.MinLength)
	}

	return nil
}

func (ValidatePasswordAdvice) After(user *User) {
	fmt.Println("ValidatePasswordAdvice after")
	fmt.Printf("password:%s validate sucess\n", user.Pass)
}

// UserAdviceGroup 通知管理组
type UserAdviceGroup struct {
	items []UserAdvice
}

// Add 注入可选通知
func (g *UserAdviceGroup) Add(advice UserAdvice) {
	g.items = append(g.items, advice)
}

func (g *UserAdviceGroup) Before(user *User) error {
	for _, item := range g.items {
		if err := item.Before(user); err != nil {
			return err
		}
	}
	return nil
}

func (g *UserAdviceGroup) After(user *User) {
	for _, item := range g.items {
		item.After(user)
	}
}

// UserProxy 代理，也是切面
type UserProxy struct {
	user *User
}

// NewUser return UserProxy
func NewUser(name, pass string) UserProxy {
	return UserProxy{user: &User{Name: name, Pass: pass}}
}

// Auth 校验，切入点
func (p UserProxy) Auth() {
	group := UserAdviceGroup{}
	group.Add(&ValidatePasswordAdvice{MaxLength: 10, MinLength: 6})
	group.Add(&ValidateNameAdvice{})

	// 前置通知
	if err := group.Before(p.user); err != nil {
		panic(err)
	}

	// 实际逻辑
	p.user.Auth()

	// 后置通知
	group.After(p.user)
}
