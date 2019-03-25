
local Article = {}
local self = Article

Article.model = require('model/article') --引入article模型
Article.userModel = require('model/article_user')

--[=[
    列表数据 自动
]=]
function Article.list()
    local list = nil

    if not ngx.ctx.uid then
        list = self.model:new():getPage(0)
    else
        local act = ngx.req.get_headers()['actionstr']
        list = self.userModel:new({act=act}):getPage()
    end
    code:outputJson(list)

end

function Article.pageList(params)
    local page = params['page']
    local list = self.model:new():getPage(page)
    code:outputJson(list)
end


--[=[
    内容页数据
    @param params table id内容id
]=]
function Article.read(params)
    local id = params['id']
    local read = self.model:new():getFind(id)
    code:outputJson(read)
end

return Article