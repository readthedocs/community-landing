const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");

module.exports = {
  performance: {
    hints: false
  },
  entry: {
    theme: ["./src/site.js", "./src/site.less"]
  },
  output: {
    filename: "js/[name].js?[hash]",
    path: path.resolve(__dirname, "_themes/landing/static")
  },
  optimization: {
    minimizer: [new OptimizeCSSAssetsPlugin({})]
  },
  module: {
    rules: [
      {
        test: require.resolve("./src/site.js"),
        use: "imports-loader?this=>window"
      },
      {
        test: /\.less$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader
            /*
            options: {
              hmr: false,
              reloadAll: true
              }*/
          },
          {
            loader: "css-loader"
          },
          {
            loader: "less-loader"
          }
        ]
      },
      {
        test: /\.(jpe?g|png|woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
        use: [
          {
            loader: "file-loader",
            options: {
              name: "[name].[ext]?[hash]",
              outputPath: "css/fonts/",
              publicPath: "fonts/"
            }
          }
        ]
      }
    ]
  },

  resolve: {
    alias: {
      // This is required to override the semanticui theme.config
      "../../theme.config": path.join(__dirname, "src/theme/theme.config"),
      "../../src/theme/site": path.join(__dirname, "src/theme/site")
    },
    extensions: [".less", ".js", ".json"]
  },

  plugins: [
    new MiniCssExtractPlugin({
      filename: "css/[name].css?[hash]",
      chunkFilename: "css/[name].css?[hash]"
    })
  ]
};
