

const state = {
    dataTabs:[
        {
            title:'首页',
            name:'home',
            content:'<h1>123</h1>首页内容',
            closable:false  //标签不可关闭
        }
    ]
}

const mutations = {
    /**
     * 新增标签
     * @param {*} state 
     * @param {object} config title:标题 name:标识 content:内容
     */
    tabAdd(state,config){
        state.dataTabs.push({
            title:config.title,
            name:config.name,
            content:config.content,
            closable:true  //标签可关闭
        })
    },

    tabRemove(state,name){
        let data = [];
        let nameActive;
        this.dataTabs.forEach((item,k) => {
            if(item.name!=name){
                data.push(item);
                nameActive = item.name
            }
        });
        this.dataTabs = data
        this.nameActive = nameActive
    }
}
export default {
    namespaced: true,
    state:state,
    mutations:mutations
  }