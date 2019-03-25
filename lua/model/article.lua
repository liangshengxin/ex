local Article = {
    hash='article:hash:id:', -- 资讯信息键名前缀 保存内容
    set_group='article:set:group:',  --分组键名前缀 保存为个组中分配的内容id 无内容前缀
    zset='article:zset:groups', -- 总组 保存各组的键名id 不含前缀
    redis=nil, --redis连接
}


-- 随机表 先放这
local function random_table(t, num) 
    for i,v in pairs(t) do 
        local r = math.random(#t)
        local temp = t[i] 
        t[i] = t[r] 
        t[r] = temp 
    end 
    num = num or #t 
    for i = #t,num+1, -1 do 
        t[i] = nil 
    end 
    return t 
end



-- 初始化配置
function Article:new(config)
    init = {}
    -- 初始配置
    if config then
        for k,v in pairs(config) do init[k] = v end
    end
    
    -- 连接redis
    if not self.redis then
        self.redis = redis:connect()
    end
    setmetatable(init,{__index=self})
    return init
end


--[=[
    获取列表数据 每页10条
    @param page int 默认0 第一页（组）
    @param articleGroupid table 传入此时page参数失效  手动传入一组的信息id
    @return table 列表信息
]=]
function Article:getPage(page,articleGroupid)
    local data = {}
    local page = page or 0 -- 0第一组
    local pageOne = articleGroupid or self:getAllID(page,page) -- 获取一组数据
    for k,id in pairs(pageOne) do
        data[k] = self:get(id,'title','media_avatar_url','source','id','behot_time','image_url','chinese_tag','category','summary')
    end
    
    return random_table(data)
end


--[=[
    获取内容页数据
    @param id int 内容id
    @return table 内容页数据
]=]
function Article:getFind(id)
    return self:get(id)
end



--[=[
    获取资讯信息下标ID 默认所有
    @param pageStart int 默认0  开始位置
    @param pageEnd int 默认-1   结束位置
    @param groupIds table 默认全部  组id
    @return table 资讯信息下标ID表
]=]
function Article:getAllID(pageStart,pageEnd,groupIds)
    
    local pageStart = pageStart or 0
    local pageEnd = pageEnd or -1
    local cRange = groupIds or self.redis:zRevRange(self.zset,pageStart,pageEnd) -- 组id 单重表格

    local data = {} --数据
    
    for oneK,groupId in pairs(cRange) do
        -- 获取每组中保存的内容id 单重表格
        local groups = self.redis:sMembers(self.set_group..groupId)
        for gk,id in pairs(groups) do
            table.insert(data,id)
        end
    end
    return data
end

--[=[
    获取单条内容数据
    @param keyID 内容数据的 redis下标id（和内容id相同）
    @params ... 可选可变参数 默认输出所有字段和值 输入参数时输出指定字段和值
]=]
function Article:get(keyID,...)
    local data = {}
    if select('#',...)~=0 then
        items = self.redis:hmGet(self.hash..keyID,...)
        for k,value in pairs(items) do
            data[table.remove({...},k)] = value
        end
        return data
    end

    local content = self.redis:hGetAll(self.hash..keyID)
    return self.redis:array_to_hash(content)
end

return Article