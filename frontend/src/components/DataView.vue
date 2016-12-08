<template>
    <div>
        <h1>{{title}}</h1>
        <hr>
        <ul v-for="(value, key) in data">
            <li>{{key}}: {{value}}</li>
            <hr>
        </ul>
    </div>
</template>

<script>
    export default {
        props: ['title', 'data']
    }
</script>

<style scoped>
h1 {
    font-weight: 400;
}
</style>
