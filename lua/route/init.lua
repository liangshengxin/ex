-- 执行路由和初始化参数
local Init = {}


-- 路由
Init.route = require('route/route') -- 引入路由
Init.action = ngx.var.action    -- 要执行的路由

Init.route[Init.action]()   --执行路由


-- ngx.ctx.r:get_reused_times()
redis:setKeepaLive(ngx.ctx.r) -- 设置连接池