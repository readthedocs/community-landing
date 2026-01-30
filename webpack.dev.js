const path = require("path");
const merge = require("webpack-merge");
const exec = require("child_process").exec;
const WatchPlugin = require("webpack-watch-files-plugin").default;
const ShellPlugin = require("webpack-shell-plugin");
const common = require("./webpack.common.js");

module.exports = merge(common, {
  mode: "development",
  watch: true,
  devServer: {
    contentBase: path.join(__dirname, "_build/html"),
    watchContentBase: true,
    compress: true,
    hot: false,
    liveReload: true,
    publicPath: "/_static/"
  },
  plugins: [
    new WatchPlugin({
      files: ["./*.py", "./**/*.rst", "./_themes/**/*.html"]
    }),
    new ShellPlugin({
      onBuildEnd: ["make clean html"],
      // dev=false here to force every build to trigger make, the default is
      // first build only.
      dev: false
    })
  ]
});
