<template>
<div class="main">

    <el-timeline :reverse="false">
        <el-timeline-item
            v-for="(item,index) in datas"
            :key="index"
            :timestamp="item.timestamp"
            :icon="item.icon"
            :color="item.color"
            :type="item.type"
            size="large"
            placement="top"
        >
            <el-card shadow="hover">
                {{item.content}}
            </el-card>
        </el-timeline-item>
    </el-timeline>
 
    
</div>
</template>

<style>
    .main{
        /* text-align:left; */
        /* max-width:500px; */
        margin:10px;
    }
    
</style>

<script>
export default {
    name:'DbSync',
    data(){
        return{
            datas:[
                
                {
                    content:'内容1',
                    timestamp:'2019-03-06',
                    type:'success',
                    icon:'el-icon-more',
                },
                {
                    content:'内容',
                    timestamp:'2019-03-07',
                    // type:'info'
                },
                {
                    content:'内容2',
                    timestamp:'2019-03-05',
                    // type:'info'
                }
            ]
        }
    }
}
</script>