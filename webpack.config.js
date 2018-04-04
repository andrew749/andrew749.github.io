const path = require('path');

var FlowBabelWebpackPlugin = require('flow-babel-webpack-plugin');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  entry: {
    // JS files
    main: './src/index.js',
    blog_main: './src/blog_main.js',

    // STYLES
    main: './static/scss/main.scss',
    projects_style: './static/scss/projects.scss',
    blog: './static/scss/blog.scss',
    blog_post: './static/scss/blog_post.scss',
    resume: './static/scss/resume.scss',
    x400_style: './static/scss/400_style.scss',
    x500_style: './static/scss/500_style.scss'
  },
  output: {
    path: path.resolve('static/dist'),
    filename: '[name].bundle.js'
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        query: {
          presets: ['babel-preset-react', 'babel-preset-es2015'].map(require.resolve)
        }
      },
      { // regular css files
        test: /\.css$/,
        loader: ExtractTextPlugin.extract([
          'css-loader?importLoaders=1',
        ]),
      },
      { // sass / scss loader for webpack
        test: /\.(sass|scss)$/,
        use: ExtractTextPlugin.extract(['css-loader', 'sass-loader'])
      }
    ]
  },
  resolve: {
   modules: [
     path.join(__dirname, "src"),
     "node_modules"
   ]
  },
  plugins: [
    new FlowBabelWebpackPlugin(),
    new ExtractTextPlugin({ // define where to save the file
      filename: '[name].css',
      allChunks: true,
    })
  ]
}
