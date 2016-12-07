<template>
    <nav id="navbar">
        <div class="nav-wrapper">
            <a href="#" class="brand-logo">&nbsp;&nbsp;&nbsp;{{title}}</a>
        </div>
    </nav>
</template>

<script>
export default {
    name: 'navbar',
    props: ['title']
}
</script>

<style scoped>
#navbar {
    position: fixed;
}
</style>
