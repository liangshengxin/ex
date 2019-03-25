<template>
    <div>
        <el-menu
            :default-active="'home'"
            mode="horizontal"
            @select="handleSelect"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b" 
            :router="true"
        >
            <el-menu-item index="home" route="/">首页</el-menu-item>
            <el-submenu index="db">
                <template slot="title">数据管理</template>
                <el-menu-item index="db-sync" route="/db-sync">数据同步</el-menu-item>

                <el-submenu index="db-list1">
                    <template slot="title">数据库管理</template>
                    <el-menu-item index="db-list1-mysql" route="/db-list-mysql">mysql</el-menu-item>
                    <el-menu-item index="db-list1-redis" route="/db-list-redis">redis</el-menu-item>
                    <el-menu-item index="db-list1-mongodb" route="/db-list-mongodb">mongodb</el-menu-item>
                </el-submenu>
            </el-submenu>
        </el-menu>
    </div>
</template>

<script>
    export default {
        methods: {
            handleSelect(key, keyPath) {
               
            }
        }
    }
</script>