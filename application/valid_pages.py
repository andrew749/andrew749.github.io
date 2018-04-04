import os

blog_posts = {
    "big_brother",
    "hello_world",
    "mac_postmortem",
    "ongoing_challenges_creating_a_distributed_system",
    "writing_a_summarizer",
    "perils_of_transitioning_a_static_site"
}

from application.markdown_object import _getMarkdownFrontMatter
blog_post_titles = {
    _getMarkdownFrontMatter(open(os.path.join("blog", "{}.md".format(x)), 'r').read())["title"] for x in blog_posts
}
