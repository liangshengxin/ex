
 /**
 *  把html转义成HTML实体字符
 * @param str
 * @returns {string}
 * @constructor
 */
function htmlEncode(str) {
    var s = "";
    if (str.length === 0) {
        return "";
    }
    s = str.replace(/&/g, "&amp;");
    s = s.replace(/</g, "&lt;");
    s = s.replace(/>/g, "&gt;");
    s = s.replace(/ /g, "&nbsp;");
    s = s.replace(/\'/g, "&#39;");//IE下不支持实体名称
    s = s.replace(/\"/g, "&quot;");
    return s;
}

/**
 *  转义字符还原成html字符
 * @param str
 * @returns {string}
 * @constructor
 */
function htmlRestore(str) {
    var s = "";
    if (str.length === 0) {
        return "";
    }
    s = str.replace(/&amp;/g, "&");
    s = s.replace(/&lt;/g, "<");
    s = s.replace(/&gt;/g, ">");
    s = s.replace(/&nbsp;/g, " ");
    s = s.replace(/&#39;/g, "\'");
    s = s.replace(/&quot;/g, "\"");
    return s;
}

// 转义字符还原成html字符
function HTMLDecode ( input ) 
{ 
    var converter = document.createElement("DIV"); 
    converter.innerHTML = input; 
    var output = converter.innerText; 
    converter = null; 
    return output; 
}

// 显示时间
function showTime(time){
    var date = new Date()
    var show = null
    // 当前时间和发布时间 间隔时间戳
    var diffTime = parseInt(date.getTime()/1000) - time
    switch (true) {
        // 5分钟内显示
        case diffTime-60*5 < 0:
            show='刚刚'
            break;
        // 30分钟内
        case diffTime-60*30 < 0:
            show=parseInt(diffTime/60)+'小时前'
            break;
        // 24小时内
        case diffTime-3600*24 < 0:
            show=parseInt(diffTime/3600)+'小时前'
            break;
        default:
            var temDate = new Date()
            temDate.setTime(time*1000)
            
            var month = temDate.getMonth()+1 //月
            var day = temDate.getDate() //日
            if (day<10) day = '0'+temDate.getDate()
            if (month<10) month = '0'+(temDate.getMonth()+1)

            // 是否同年
            
            if (temDate.getFullYear() == date.getFullYear()){
                show = month+'-'+day
            }else{
                show = temDate.getFullYear()+'-'+month+'-'+day
            }
            break;
    }
    
    return show
}

const state = {
    datas:{
        headimg:'http://demo.cssmoban.com/cssthemes4/amz_17_bef/img/a4.png',
        name:'中国社会网',
        showtime:'2小时前',
        title:'华为折叠屏手机要看韩国人脸色？OLED面板产能今年有望华丽转身',
        content:'华为折叠屏手机要看韩国人脸色？OLED面板产能今年有望华丽转身',
    },
    showBool:'loading', //loading显示正在加载 error加载失败 success显示内容
}


const mutations = {
    initGet(state,id){
        axios.get(this.state.host+'/article?id='+id)
            .then(function(response){
                var res = response.data.data
                var conts={
                    headimg:res.media_avatar_url,
                    name:res.source,
                    showtime:showTime(res.behot_time),
                    title:res.title,
                    content:res.category==2?res.content:HTMLDecode(res.content) //bug 待修复 内容页实体字符转换问题 csdn的无需转换 头条的需要转换
                }
                state.datas = conts
                state.showBool='success'
            })
            .catch(error => {
                state.showBool='error'
                console.log(error)
            })
            .then(function(){
                // toast.hide()
            })
            // .finally(() => )
            
    }
}
export default {
    namespaced: true,
    state:state,
    mutations:mutations
}