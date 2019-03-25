
local Method = {}

Method.method = string.lower(ngx.req.get_method()) -- 获取请求方式
Method.getArgs = ngx.req.get_uri_args() -- get请求参数



function Method:get(option)
    for k,item in pairs(option) do
        if self:initGet(item.action,item.params) then
            break
        end
    end
end


--[=[
    get请求执行的方法
    @param action 方法名
    @param option table 请求的参数 默认{} 格式{参数名='参数类型'} number数字 string字符串
    @return action(option)
]=]
function Method:initGet(action,option)
    local option = option or {}
    if self.method~='get' then return end

    local argLen = self:len(self.getArgs) --参数长度

    -- 无参数时执行的action
    if argLen==0 then 
        action()
        return true
    end
    
    -- 指定参数时执行的action (并验证参数个)
    if argLen~=0 and argLen==self:len(option) then
        -- 验证参数名和类型
        for field,types in pairs(option) do
            -- 类型不同取消执行
            -- if type(tonumber(self.getArgs[field]))~=types then return end
            -- 参数名验证
            if not self.getArgs[field] then return end
        end
        -- 执行方法并传入参数
        action(self.getArgs)
        return true
    end
end


-- 获取表长度
function Method:len(tabs)
    local len = 0
    for k,v in pairs(tabs) do
        len = len+1
    end
    return len
end

return Method