<template>
    <!-- 封面使用视频的第一帧 -->
    <video :src="item.url" :poster="" controls></video>
    <!-- 图片也可以用， 只需要在地址后面加这一段代码就可以了   '?x-oss-process=video/snapshot,t_0,f_jpg' -->
    <image class="cover" :src="item.url+ '?x-oss-process=video/snapshot,t_0,f_jpg'" mode=""></image>
<template>
<script lang=ts setup>
    const src = "sssss"
</script>
<style>

</style>
    
    