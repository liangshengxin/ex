

-- 按用户分配信息

local ArticleUser = {
    act="refresh",  -- 用户的行为 refresh刷新  load加载  必传
    user_groups='article:user:zset:groups:uid:', -- 对应用户访问过的组id有序集合
    article=nil, --article模型
    timeout=3600*3, --用户浏览记录数据保存时长 秒
}


function ArticleUser:new(config)
    init = {}
    if config then
        for k,v in pairs(config) do init[k] = v end
    end

    self.article = require('model/article')
    setmetatable(init,{__index=self})

    if not ngx.ctx.uid then ngx.exit('403') end -- 检测uid

    return init
end

-- 获取符合要求的资讯信息
function ArticleUser:getPage()
    local userKey = self.user_groups..ngx.ctx.uid -- 指定用户集合键名
    local cRange = nil
    if self.act=='refresh' then
        cRange = self:groupUpId(userKey) -- 只刷新最新的100组
    else
        cRange = self:groupUpId(userKey) -- 先加载最新的
        if not cRange then 
            cRange = self:groupDownId(userKey) -- 没有则继续向下加载
            if not cRange then
                cRange = self:groupUpId(userKey,true) --还没有则清除浏览记录从新加载
            end
        end
    end
    local articleGroupid = self.article:getAllID(0,0,{cRange})
    local data = self.article:new():getPage(nil,articleGroupid)
    return data
end


-- 获取用户还未访问的最高分值的组id
-- @param isUnset true|false  true清空指定用户记录  默认false
-- @return groupUpid | nil 未获取到
function ArticleUser:groupUpId(userKey,isUnset)
    
    if isUnset then ngx.ctx.r:del(userKey) end

    local groupUp = ngx.ctx.r:zRevRange(userKey,0,0) --用户最高组id  table[1] | nil
    local groupUpId = nil -- 还未访问的最高组id 
    if groupUp[1] then
            -- 查找最新的未访问组id 范围 0~100
            for k,id in pairs(ngx.ctx.r:zRevRange(self.article.zset,0,100)) do
                --检查是否访问过
                local isRead = ngx.ctx.r:ZSCORE(userKey,id)
                if type(isRead)~='string' then
                    -- 未访问过 赋值 跳出
                    groupUpId = id
                    break
                end
            end
        
    else
        -- 用户组不存在时 直接从源数据获取最新
        groupUpId = ngx.ctx.r:zRevRange(self.article.zset,0,0)[1]
    end
    -- 存在时存入用户组集合
    if groupUpId then
        ngx.ctx.r:zadd(userKey,os.time(),groupUpId)
        self:timeOut(userKey)
    end
    return groupUpId
end

-- 获取用户需要加载的下一组id
-- @return groupDownid | nil 未获取到
function ArticleUser:groupDownId(userKey)

    -- 获取用户访问的最低分值的组id
    local groupDown = ngx.ctx.r:zRevRange(userKey,0,0) --  --用户最低组id table[1] | nil
    local groupDownId = nil -- id
    if groupDown[1] then
        local groupNews = ngx.ctx.r:ZREVRANGEBYLEX(self.article.zset,'('..groupDown[1],'-','limit',0,1) -- (不包含自身
        if groupNews[1] then
            groupDownId=groupNews[1]
        end
    else
        -- 用户组不存在时 直接从源数据获取最新
        groupDownId = ngx.ctx.r:zRevRange(self.article.zset,0,0)[1]
    end
    -- 存在时存入用户组集合
    if groupDownId then
        ngx.ctx.r:zadd(userKey,os.time(),groupDownId)
        self:timeOut(userKey)
    end
    return groupDownId
end

-- 设置k生存时间
function ArticleUser:timeOut(key)
    local ttlect = ngx.ctx.r:TTL(key) - 1800
    if (not ttlect) or ttlect<0 then 
        ngx.ctx.r:EXPIRE(key,self.timeout)
    end
end

return ArticleUser;