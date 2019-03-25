--[=[
    redis连接
    redis = require('redis') 引入
    r = redis:new({ip='xxx'}) 或者 redis:connect()
    r:set('key','val')
]=]



local Redis = {
    ip='127.0.0.1', --ip
    port=6379,     --端口
    timeout=1000,  --超时时间毫秒
    line_max_time=1000*10, -- 连接池时间 毫秒
    line_size=100, -- 连接池大小
    r=nil,
}

Redis.redis = require('resty.redis') -- 引入redis

-- 初始化redis 配置连接 
function Redis:new(config)
    local init = {}
    for key,value in pairs(config) do
        init[key] = value
    end
    setmetatable(init,{__index=self})
    return init
end

-- 连接redis
function Redis:connect()
    local r = self.redis:new()  --初始化
    r:set_timeout(self.timeout) -- 超时时间
    local ok,err = r:connect(self.ip,self.port) -- 获取连接
    if not ok then
        ngx.say('redis连接失败:'..err)
        return nil
    end
    self.r = r
    return r
end

-- 设置连接池 r  redis实例
function Redis:setKeepaLive(r)
    local ok,err = r:set_keepalive(self.line_max_time,self.line_size) -- 设置连接池
    if not ok then
        ngx.say("set keepalive error:"..err)
    end
end

return Redis