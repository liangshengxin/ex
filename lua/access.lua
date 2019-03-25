--[=[
    请求验证 | 初始值
]=]


-- ip验证
if false then
    ngx.exit(403)
end

-- 请求头验证
if false then
    ngx.exit(403)
end

-- 解密验证
if false then
    ngx.say('{"code":"0","data":"","msg":"请求失败"}')
    ngx.exit(403)
end


-- 设置全局 redis 实例
ngx.ctx.r = redis:connect()

ngx.ctx.get_method = string.lower(ngx.req.get_method()) -- 获取请求方式 小写
ngx.ctx.get_uri_args = ngx.req.get_uri_args() -- 获取get请求参数

ngx.ctx.uid = ngx.req.get_headers()['uid'] -- 用户uid