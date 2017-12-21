// @flow

import React from 'react';

type ListElementProps = {
  title: string,
  subtitle: string,
  tertiaryTitle?: string,
  imageUrl?: string
}

export default class ListElement extends React.Component<ListElementProps> {
  render() {
    var tertiaryTitle;
    var imageThumbnail;

    if (this.props.tertiaryTitle) {
      tertiaryTitle = <h6 className="tertiary-title">{this.props.tertiaryTitle}</h6>
    }

    if (this.props.imageUrl) {
      imageThumbnail = (<div className="list-element-image-container">
          <img className="list-element-image" src={this.props.imageUrl}/>
        </div>);
    }


    return (
      <div className="list-element">
        <div className="list-element-text-container">
          <h4>{this.props.title}</h4>
          <p>{this.props.subtitle}</p>
          {tertiaryTitle}
        </div>
        {imageThumbnail}
      </div>
    )
  }
}
