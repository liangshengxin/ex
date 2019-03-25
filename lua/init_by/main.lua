
cjson = require("cjson") -- json解析

redis = require("module/redis") -- return redis
base64 = require("module/outside/base64") -- base64编码
aes = require("module/aes") -- aes加密

code = require("module/code") -- 格式化输出数据

math.randomseed(os.time()) -- 随机数种子