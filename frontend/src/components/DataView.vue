<template>
    <div>
        <h5>{{title}}</h5>
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
