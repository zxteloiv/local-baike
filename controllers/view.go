package controllers

import (
	"github.com/zxteloiv/local-baike/models"
	//"encoding/json"

	"github.com/astaxie/beego"
)

// Operations about View
type ViewController struct {
	beego.Controller
}

// @Title Get
// @Description get user by uid
// @Param	uid		path 	string	true		"The key for staticblock"
// @Success 200 {object} models.User
// @Failure 403 :uid is empty
// @router /:uid [get]
func (vc *ViewController) Get() {
	id := vc.GetString(":id")
	if id != "" && models.ExistsView(id) {
        view, _ := models.GetView(id)
        vc.Ctx.WriteString("Hello World")
        vc.Ctx.WriteString(view.Data)
	}
}

