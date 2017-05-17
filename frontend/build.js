var fs = require('fs');
var browserify = require('browserify');
var vueify = require('vueify');
var envify = require('envify/custom');
var errorify = require('errorify');

node_env = process.env.NODE_ENV || 'development';

browserify('src/index.js')
    .plugin(errorify)
    .transform(vueify)
    .transform(
        envify({
            _: 'purge',
            NODE_ENV: node_env
        }),
        {
            global: true
        }
    )
    .plugin('vueify/plugins/extract-css', {
        out: 'src/.build.css'
    })
    .bundle()
    .pipe(fs.createWriteStream('src/.build.js'));
