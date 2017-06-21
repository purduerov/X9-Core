<template>
    <nav id="navbar">
        <div class="nav-wrapper">
            <span id="title">{{title}}</span>
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
    width: 100%;
}

.nav-wrapper {
    background-color: #37474f;
}

#title {
    font-weight: 100;
    font-family: 'Roboto', Helvetica, Arial, sans-serif;
    padding-left: 28px;
    line-height: 50px;
    font-size: 20px;
    color: white;
}

</style>
