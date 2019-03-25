
const state = {
    datas:[],
    options:{
        //下拉刷新配置
        pullDownRefresh: {
            threshold:50,
            txt:'刷新成功'
        },
        // 上拉加载配置
        pullUpLoad: {
            threshold:90,
            txt:{
                more:'',
                noMore:'暂无更多内容'
            }
        },
        scrollbar: {fade:true}, // 滚动条隐藏
        // probeType:1, // 派发scroll事件
    },
    // page:0,  //初始页数
    scrollEndY:0, //滚动停止时的位置 Y
    domnScroll:100, //菜单中下按钮元素 距离顶部的距离 <2时触发一次允许滚动（默认的时候大于2 避免初始时触发）

    showBool:'loading', //loading显示正在加载 error加载失败 success显示内容
}

/**
 * 
 * @param {object} _this state实例
 * @param {object} _scrollThis scroll实例
 * @param {string} action 动作 refresh刷新 load加载 必传 默认load
 * @param {object} params 发送的参数
 * @param {callback} callback 加载成功回调
 */
function initGet(_this,_scrollThis,actionStr,params,callback){
    axios.get(_this.state.host+'/article',{
        timeout: 5000,
        headers: {
            Uid:_this.state.uid,
            Authorization:'123456',
            ActionStr:actionStr || 'load'
        },
        params:params
    })
        .then(function(response){
            var datas = false
            if(response.data.code==200 && response.data.data[0]){
                datas = []
                response.data.data.forEach((item,k) => {
                    datas[k] = {
                        id:item.id, //id
                        behot_time:item.behot_time, //发布时间
                        image:item.image_url, //封面
                        headimg:item.media_avatar_url, //用户头像
                        name:item.source, //用户
                        title:item.title, //标题
                        synopsis:item.summary || item.title, //说明
                        category:item.category, //类别
                        type: item.chinese_tag,//类别名称
                    }
                });
            }
            callback(datas)

            if (!datas){
                _scrollThis.$refs.scroll.forceUpdate() //无新内容时执行
            }
        })
        .catch(error => {
            _scrollThis.$refs.scroll.forceUpdate()
            console.log(error)
            _scrollThis.$createToast({
                time:1000,
                txt: '加载失败',
                type: 'txt'
            }).show()
            
        })
        .then(function(){
            // toast.hide()
        })
        .finally(function(){
            // 
            _this.state.homeInfoScroll.showBool='end'
        })
}

const mutations = {
    // 初始加载
    onPullingStart(state,_this){
        initGet(this,_this,'load',null,function(datas){
            if(datas){
                datas.forEach(item => {
                    state.datas.unshift(item)
                });
            }
            if(state.domnScroll>2){ //大于2时触发发禁止滚动
                _this.$refs.scroll.disable()
            }
        })

    },
    // 下拉刷新
    onPullingDown(state,_this){
        initGet(this,_this,'refresh',null,function(datas){
            if(datas){
                datas.forEach(item => {
                    state.datas.unshift(item)
                });
            }else{
                _this.$createToast({
                    time:1000,
                    txt: '暂无更多内容',
                    type: 'txt'
                }).show()
            }
        })
    },
    // 上啦加载
    onPullingUp(state,_this){
        initGet(this,_this,'load',null,function(datas){
            if(datas){
                state.datas = state.datas.concat(datas)
            }
        })
    }
}
export default {
    namespaced: true,
    state:state,
    mutations:mutations
}