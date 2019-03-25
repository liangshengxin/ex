local Code = {
    code=200,
    data={},
    msg='ok'
}


-- 输出json格式数据
function Code:outputJson(tabs)
    ngx.say(
        cjson.encode({
            code = self.code,
            data = tabs,
            msg = self.msg
        })
    )
end


-- 返回json格式数据
function Code:json(tabs)
    return cjson.encode({
        code = self.code,
        data = tabs,
        msg = self.msg
    })
end


return Code