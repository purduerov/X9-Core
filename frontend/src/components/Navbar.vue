<template>
    <nav id="navbar">
        <div class="nav-wrapper">
            <a href="#" id="title">{{title}}</a>
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

.nav-wrapper {
    background-color: #009688;
}

#title {
    font-weight: 100;
    font-family: 'Roboto', Helvetica, Arial, sans-serif;
    padding-left: 28px;
    line-height: 50px;
}

</style>
