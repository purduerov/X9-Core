<template>
    <div id="container">
        <div id="card">
            <div id="main-container" :style="{backgroundColor: color}">
                <div v-if="title !== undefined" id="title">{{title}}</div>
                <div id="padding">
                    <slot></slot>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['title', 'color']
    }
</script>

<style scoped>
#container {
    width: 100%;
}

#card {
    font-family: 'Roboto', Helvetica, Arial, sans-serif;
    width: 100%;
    height: 100%;
    position: relative;
    box-sizing: border-box;
    padding: 10px;
    color: white;
    overflow: hidden;
}

#main-container {
    width: 100%;
    height: 100%;
    min-height: 100px;
    background-color: #2e2e2e;
    box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
}

#padding {
    box-sizing: border-box;
    padding: 10px;
    width: 100%;
    height: 100%;
    overflow: hidden;
}

#title {
    height: 35px;
    line-height: 35px;
    font-size: 24px;
    color: white;
    background-color: rgba(0,0,0,0.2);
    padding: 0 10px;
}
</style>
