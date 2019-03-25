--[=[
    redis连接
    redis = require('redis') 引入
    r = redis:new({ip='xxx'}) 或者 redis:connect()
    r:set('key','val')
]=]



local Redis = {
    ip='127.0.0.1', --ip
    port=6379,     --端口
    timeout=1000  --超时时间毫秒
}

Redis.redis = require('resty.redis') -- 引入redis

-- 初始化redis 配置连接 
function Redis:new(config)
    local init = {}
    for key,value in pairs(config) do
        init[key] = value
    end
    setmetatable(init,{__index=self})
    return self:connect()
end

-- 连接redis
function Redis:connect()
    local r = self.redis:new()  --初始化
    r:set_timeout(self.timeout) -- 超时时间
    local ok,err = r:connect(self.ip,self.port) -- 获取连接
    if not ok then
        ngx.say('redis连接失败:'..err)
        r:set_keepalive() -- 设置连接池
        return nil
    end
    return r
end

return Redis