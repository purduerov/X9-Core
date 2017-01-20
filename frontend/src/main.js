var Vue = require("vue")
var App = require("./components/App.vue")

new Vue({
    el: '#app',
    render: f => f(App),
    components: {
        App
    }
})

