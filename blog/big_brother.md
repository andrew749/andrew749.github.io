---
title: Analyzing trips to the kitchen
subtitle: An exercise in OpenCV, scipy and pandas
date: Friday October 28, 2016
---

Wish had their quartely hackthon last night and I figured I should probably
write about what I did since its a pretty interesting image processing project.

For some context, in a previous hackathon an intern purchased and set up
a camera to monitor the kitchen with a live video feed. For obvious reasons
this is useful project in and of itself (instantly know when food gets to the
kitchen :P). The issue with this was that either we needed a single screen
contantly dedicated to a video feed or we would need to divert work to quickly
check the camera feed, an undesirable situation :P.

Being an Engineer, I knew that there were countless ways to improve this and
thus consqeuently streamline our lunch routine. So for my hackathon project,
I decided to create a simple python script which would use varius image
processing techniques to determine if there were people in the kitchen and send
a message to a slack channel when it though food was delivered.

## What I did

Well first things first, I needed to interface with the camera to get image
data. This was simple enough and only took something like 5 minutes due to the
VERY bad security on the ip camera.

The camera sends the username and password as url params for a webpage and each
time the url is hit, a new image is loaded. Their interface consisted of
a timer that would constantly reload an image and just update the screen
accordignly. This is terrible practice and probably why recently people have
been able to launch DDOS attacks O(1 Tbs) https://dyn.com/blog/dyn-analysis-summary-of-friday-october-21-attack/ , but I digress.

Once I was able to pull images I could then begin processing the image. Ill try
to keep this a sweet and short summary of what I did. First, images were
converted to grayscale to make processing easier and since color data wasnt
needed in any of the following steps.

The next step was to apply a Gaussian blur. This is an important step because it helps to remove noise that was
present due to the camera sensitivity.

Once noise was removed I was able to
compare frames. The current algorithm is extermely naive and just compares
consecutive keyframes. I calculated the difference between the two images and
then thresholded the result of this to try and detect major features  that changed
in between the frames. After this was done, the pipeline had a result that
resemble the silhouette of a human. I found contours on this silhouette and
then detemined the size of a bounding box around the image. After determining
bounding boxes, I thresholded these results one more time by the area of the
detected bounding box. This was tweaked manually until I found a threshold that
seemed to work well.

Finally now that I had bounding boxes for supposed people, I would once more
threshold this number and if the number of boxes was above a threshold,
I counted that frame as being "Occupied" with people. If a certain % of frames
were occupied out of the last 50, I would consider this being sufficient
traffic such that I could alert people. I debounced this limit such that
messages could not be sent withing a certain time range of one another. I'm going to skip the details of setting
up the slack bot as that is not the focus of this post.

At this point, I had a fully functional bot that would send messages to slack
when there were more than 3 people spending a sufficient amount of time in the
kitchen.

## Data Analysis

I will update this section after I have sufficient data. Early results though
seem to be relatively clean, meaning that there is a clear distinction from
when there are people in the kitchen and when there aren't, meaning no true
negatives. False positives seem to be an issue though as people seem to spend
a lot of time in the kitchen when they do go for a snack/drink :).
