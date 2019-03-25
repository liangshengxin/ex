-- 执行路由和初始化参数
local Init = {}


-- 初始化全局数据
initParams = {
    uid=ngx.req.get_headers()['uid'], --用户id
}


-- 路由
Init.route = require('route/route') -- 引入路由
Init.action = ngx.var.action    -- 要执行的路由

Init.route[Init.action]()   --执行路由