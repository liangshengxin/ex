
local Route = {}
local self = Route

Route.method = require('route/bin/method') --执行方式



-- article 路由
function Route.article()
    local init = require('content_by/article')
    Route.method:get({
        {
            action=init.list -- 列表数据 自动
        },
        {
            action=init.pageList, --列表数据 按page分页
            params={page='number'}
        },
        {
            action=init.read,   -- 内容
            params={id='number'}
        },
    })
end





return Route