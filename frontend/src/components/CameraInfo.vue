<template>
    <div>
        <div v-for="(cam,name) in data" :key="name">
            {{name}}: {{cam.status}}
            <hr />
        </div>
    </div>
</template>

<script>
export default {
    name: 'camera-info',
    props: ['data', 'status'],
}
</script>

<style scoped>
</style>