<template>
	<view class="content">
		<image class="logo" src="/static/logo.png"></image>
		<view class="text-area">
			<text class="title">{{title}}</text>
		</view>
	</view>

	<button @click="increment">Count is {{ count }}</button>
</template>

<script lang="ts" setup>
// lang="ts": script使用typescript语言
// setup

	import {ref, onMounted} from 'vue'
 	const title = 'Hello'
 	const count = ref(0)

	function 
</script>

<style lang="scss" scoped>
// lang="scss"
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	.logo {
		height: 200rpx;
		width: 200rpx;
		margin-top: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: #8f8f94;
	}
</style>
