module.exports = {
    "transpileDependencies": [
        "vuetify"
    ],
    outputDir: 'dist',
    assetsDir: 'static',
    // baseUrl: 'http://markvale15.herokuapp.com',
    // baseUrl: 'localhost:8000/static/',
    // baseUrl: IS_PRODUCTION
    // ? 'http://cdn123.com'
    // : '/',
    // For Production, replace set baseUrl to CDN
    // And set the CDN origin to `yourdomain.com/static`
    // Whitenoise will serve once to CDN which will then cache
    // and distribute
    devServer: {
        proxy: {
            '/*': {
                // Forward frontend dev server request for /api to django dev server
                target: 'http://markvale15.herokuapp.com/',
            }
        }
    }
}