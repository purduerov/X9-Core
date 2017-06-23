var Vue = require("vue")
var App = require("./App2.vue")

new Vue({
    el: '#app2',
    render: f => f(App),
    components: {
        App
    }
})
