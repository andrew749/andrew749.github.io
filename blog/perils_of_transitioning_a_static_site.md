---
title: Perils of transitioning a static site.
subtitle: More than just wrapping a bunch of pages in a router.
date: Saturday August 13, 2016
---

So as you might or might not know, my website was originally hosted on GitHub
pages. For as long as I can remember, I've been fixated with transitioning the
web site from using static pages to using some sort of templated system to
allow for more modularity and better reuse of code. Unfortunately, up until
a few days ago, school and life left me with little time to pursue this
project.

Then my sophomore year of University of ended.

Now I am writing to you mid way through the transition. I've re-written most of
the site using Flask templates using Jinja as the templating langauge. Words
cannot describe how much time this saves versus having to maintain almost
identical pages in HTML and Javascript.

## The beginning

The transition started by, ironically, wrapping a bunch of static pages in
a router. This took a whole 10 minutes. I could have called it quits, and would
have been left with a perfectly functional site that mirrored what I had
originally. But that wasn't enough, I wasn't taking advantage of the powerful
features of a web application framework.

## Refactoring

And so came the refactoring stage. Conveniently in my 2nd year of University,
there was a course related to software design patterns. This involved several
lessons in indicators that a project should be refactored and best practices of
how this should be done. For those of you privy to some of the terminology,
I found myself being able to apply functional programming concepts, such as
partial application and currying to my advantage. These language tools allow
you to very easily write very modular function than can be stringed together to
specialize the function such that it works as expected, with very little code
duplication. For example, this website uses a very simple python script to
parse markdown and update a database which stores the content to later be
rendered. Templating also allowed a lot of common code (pretty much everything
in the head tags of a website, as well as common elements like the floating
action button and the navigation bar) to be placed in a single
file which would then be specialized for more specific pages. Not only does
this save time, since you do not need to change every file if a single
dependency changes, but it also makes the code significantly simpler. I have
one point of contact where imports need to be placed, and another where all the
pages contents need to be placed. Thats it. After having built this system,
adding new pages which followed my core theme was a breeze and took very
little time. Also, since this was in the middle of a refactor, any stylistic
changes I made would propagate across the entire website.

## Deployment

This website is currently being hosted on AWS. Getting it on there was
a complete pain. For context, this is not the first time I've used AWS for
a project. Part of the reasons that I encountered much difficulty performing
this transition was the fact that AWS uses hidden folders and non-existent
configuration files to configure a project. For example, this website has the
server contained in a router called `app.py` with a Flask module named `app`.
Amazon does not like this. Apparently, they expect the main server file to be
named `application.py` and the module to thus be called `application` contrary
to normal Flask convention. After a bunch of googling I finally determined that
Elastic Beanstalk EXPECTS you to create a hidden folder called `.ebextensions`
and to also create a file with the name of your environment. This file
essentially provides additional information for Elastic Beanstalk to configure
itself outside of the default settings. Below is a snippet of what I had to
include for my website.

    option_settings:
      - namespace: aws:elasticbeanstalk:container:python
        option_name: WSGIPath
        value: app.py


So as you can see, I specify a namespace for the container (how Elastic
Beanstalk determines what type of environment you are running since all
applications need to be placed in a container), as well as a key `WSGIPath` and
finally the value for the key. Though the process was not extremely
straighforward, I found that after a little research, the true power of
Amazon's command line tool started to come to light.

> Andrew
