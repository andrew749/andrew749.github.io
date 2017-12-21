// @flow

import React from 'react';
import ReactDOM from 'react-dom';

import ListElement from './list-element';

type ProjectsPageProps = {
}

type ProjectsPageState = {
  projects: Project[]
}

type Project = {
  title: string,
  subtitle: string,
  projectSlug: string,
  url: string,
  thumbnailPath?: string
}

export default class ProjectsPage extends React.Component<ProjectsPageProps, ProjectsPageState> {
  constructor() {
    super()
    const projects:Array<Project> = []
    this.state = {
      projects: projects
    }
  }

  componentDidMount() {
    fetch("/api/getProjects").then((res) => {

      if ( res && res.json && this.state && this.setState != undefined) {
        res.json().then(projects => {
          this.setState({projects:  projects})
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
          this.state.projects.map((project) => {
            return (
              <a href={project.url}>
                <ListElement
                  onClick= { () => { window.location = project.url; } }
                  title={ project.title }
                  subtitle={ project.subtitle }
                  imageUrl={ project.thumbnailPath } />
              </a>
            )
          })
        }
      </div>
    )
  }
}

const container = document && document.getElementById('container');

if (container) {
  // render the page
  ReactDOM.render(
    <ProjectsPage />,
    container
  );
}
