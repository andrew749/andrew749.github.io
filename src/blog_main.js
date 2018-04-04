// @flow

import React from 'react';
import ReactDOM from 'react-dom';
import ListElement from './list-element';

type BlogPageProps = {
}

type BlogPageState = {
  posts: Post[]
}

type Post = {
  title: string,
  subtitle: string,
  url: string,
  date?: string,
}

export default class BlogPage extends React.Component<BlogPageProps, BlogPageState> {
  constructor() {
    super()
    const posts: Array<Post> = []
    this.state = {
      posts: posts
    }
  }

  componentDidMount() {
    fetch("/api/getBlogPosts").then((res) => {

      if ( res && res.json && this.state && this.setState != undefined) {
        res.json().then(posts => {
          this.setState({posts:  posts})
        });
      }

    }).catch((error)=> {
      console.error(error);
    });
  }

  render() {
    return (
        <div className="project-list">
          {
            this.state.posts.map((post) => {
              return (
                <a href={post.url}>
                  <ListElement
                    title={ post.title }
                    subtitle={ post.subtitle }
                    tertiaryTitle={ post.date } />
                </a>
              )
            })
          }
        </div>
    )
  }
}

const container = document && document.getElementById('post_container');

if (container) {
  // render the page
  ReactDOM.render(
    <BlogPage />,
    container
  );
}
