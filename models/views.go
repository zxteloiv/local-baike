package models

import (
	"errors"
	//"strconv"
	//"time"
)

func init() {
}

type View struct {
    // {"itemid": "1000036.htm", "url": "http://baike.baidu.com/view/1000036.htm", "itemtype": "view", "anchor": ""}
    ItemId   string
    Url      string
    ItemType string
    Anchor   string
    Data     string
}

func GetRandomView() (View, error) {
    return View{}, nil
}

func GetView(itemid string) (View, error) {
    return View{}, errors.New("not implemented")
    return View{}, nil
}

func GetSubView(id, subid string) (View, error) {
    return View{}, nil
}

func ExistsView(id string) bool {
    return true
}

func ExistsSubView(id, subid string) bool {
    return true
}

