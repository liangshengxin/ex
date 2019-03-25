--[=[
    aes加解密
    请确认base64模块以全局引入
    使用方法
        aes = require('aes') 引入
        init = aes:new({key=xxx,...}) 初始化配置（可省略初始化）
        action = init:Aes:cbc128Md5() 加解密方式
        enc = action:encrypt('xxx')   加密  接收字串             返回的加密数据经过base64编码
        dec = action:decrypt(enc)     解密  接收base64解码后密码 返回原始字串
    加密解密方法
        cbc128Md5     AES 128 CBC IV 无盐 无轮次
        cbc256Sha512  AES 256 CBC 盐 sha512密钥 轮次 无向量
]=]


local Aes = {
    key='1234567890123456', -- 密钥 16位
    salt='m2a45678', -- 盐值 8个字符或nil
    iv="1234567890123456",   -- 密钥向量 16位
    rounds=1,        -- 加密密钥轮次
    
}

-- 加载aes模块
Aes.aes = require('resty.aes')

-- 加解密方式
local localAes = nil

-- 初始化修改配置 config 表 {key='xxx'}
function Aes:new(config)
    local init={}
    for key,value in pairs(config) do
        init[key] = value
    end
    setmetatable(init,{__index=self})
    return init
end

-- AES 128 CBC IV 无盐 无轮次
function Aes:cbc128Iv()
    localAes = self.aes:new(self.key, nil, self.aes.cipher(128,"cbc"), {iv=self.iv})
    return self
end

-- AES 256 CBC 有盐 sha512密钥 有轮次 无向量
function Aes:cbc256Sha512()
    localAes = self.aes:new(self.key, self.salt, self.aes.cipher(128,"cbc"), self.aes.hash.hash512, self.rounds)
    return self
end



-- 加密  str加密字符串 返回base64转码后数据
function Aes:encrypt(str)
    if not localAes then error('请选用加密方式') end
    return base64.enc(localAes:encrypt(str))
end

-- 解密  str解密字符串 经过base64编码的数据
function Aes:decrypt(str)
    if not localAes then error('请选用解密方式') end
    return localAes:decrypt(base64.dec(str))
end




return Aes