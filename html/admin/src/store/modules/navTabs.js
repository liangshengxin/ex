

const state = {
    // 初始数据
    dataTabs:[
        {
            title:'首页',
            name:'/',
            content:'<h1>123</h1>首页内容',
            closable:false  //标签不可关闭
        }
    ],
    nameActive:'/', //默认选中
}

const mutations = {
    /**
     * 新增或移动 标签
     * @param {*} state 
     * @param {object} config title:标题 name:标识 content:内容
     */
    tabAdd(state,config){
        let isActionName = false
        state.dataTabs.forEach(item=>{
            if(item.name==config.name) {
                isActionName = config.name 
                return false
            }
        })
        if(!isActionName){
            state.dataTabs.push({
                title:config.title,
                name:config.name,
                content:config.content,
                closable:true  //标签可关闭
            })
            isActionName = config.name 
        }
        state.nameActive = isActionName
    },

    /**
     * 删除标签
     * @param {*} state 
     * @param {string} name 标签name标识
     */
    tabRemove(state,name){
        let _this = this
        let data = [];
        let nameActive;
        state.dataTabs.forEach((item,k) => {
            if(item.name!=name){
                data.push(item);
                nameActive = item.name
            }
        });
        state.dataTabs = data
        state.nameActive = nameActive
        console.log(state)
    },

    /**
     * 移动到指定标签
     * @param {*} state 
     * @param {string} name 标签name标识
     */
    tabMove(state,name){
        state.nameActive = name
    },


    tabClick(state,tabObj){
        console.log(tabObj)
    }
}
export default {
    namespaced: true,
    state,
    mutations,
}