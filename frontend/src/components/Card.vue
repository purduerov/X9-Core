<template>
    <div>
        <div id="card">
            <div id="main-container" :style="{backgroundColor: color}">
                <div id="padding">
                    <slot></slot>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['color']
    }
</script>

<style scoped>
#card {
    font-family: 'Roboto', Helvetica, Arial, sans-serif;
    width: 100%;
    height: 100%;
    position: relative;
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
    transition: all 0.3s cubic-bezier(.25,.8,.25,1);
    border-radius: 2px;
}

#padding {
    padding: 10px;
    width: 100%;
    height: 100%;
    overflow: hidden;
}
</style>
