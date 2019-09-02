module.exports = {
  lintOnSave: false,
  filenameHashing: false,
  productionSourceMap: false,

  devServer: {
    proxy: 'http://localhost:5000'
  },

  pluginOptions: {
    i18n: {
      locale: 'en',
      fallbackLocale: 'en',
      localeDir: 'locales',
      enableInSFC: true
    }
  }
}
