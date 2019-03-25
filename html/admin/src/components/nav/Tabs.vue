<template>
    <div class="mains">
        <el-tabs
            v-model="$store.state.navTabs.nameActive"
            type="card"
            @tab-click="tabObj=>$store.commit('navTabs/tabClick',tabObj)"
            @tab-remove="name=>$store.commit('navTabs/tabRemove',name)"
        >
            <el-tab-pane
                v-for="(item,index) in $store.state.navTabs.dataTabs"
                :key="item.name"
                :label="item.title"
                :name="item.name"
                :closable="item.closable"
            >
                <!-- <router-view></router-view> -->
                <div v-html="item.content"></div>
            </el-tab-pane>
            
            <!-- <el-tab-pane label="管理" name="one">管理</el-tab-pane>
            <el-tab-pane label="2" name="two">2</el-tab-pane>
            <el-tab-pane>
                <span slot="label"><i class="el-icon-date"></i>自定义内容</span>
                我的行程
            </el-tab-pane> -->
        </el-tabs>
    </div>
</template>

<script>
export default {
    
}
</script>