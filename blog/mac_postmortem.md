---
title : Postmortem for my Mac
subtitle : Some general lessons learned from what could have been a devastating loss.
date: Saturday January 28, 2017
---

## Story
One of the things that one dreads as a Software Engineer is the lost of your
trusty workstation.  This could be compounded if you weren't adament at keeping
backups for the device and hours, or even days, of work are lost.

This happened to me today. After getting up, I was suprised to find that my
laptop, still plugged in, didn't have any power indicator light on. I figured
this was just a bad connection and tried reconnecting the cable. Nothing.

I then tried another outlet, maybe a fuse was tripped overnight and there was
no power. Still Nothing.

In an early state of panic I tried booting up my computer to test my fears.
After several minutes of repeatly holding the power button, resetting the SMC
(as advised on several forums) my laptop was still seemingly dead. I called up
Apple Support, hoping that they could shed some light on the issue but
unfortunately, they just reaffirmed my suspicions that there was something
majorly wrong with my computer.

Heeding Apple's advice, I went to my closest Apple store and scheduled a walk
in appointment with one of their so called "geniuses". After waiting close to
2 hours for service they tried the same diagnostics that Apple support walked
me through to no avail. They took my laptop to the back of the store to open it
up and possibly try resetting the SMC through hardware. I was left waiting.

For what seemed like an eternity, I was trying to recall what sort of backups
I had kept. I had remembered that the day before, I took the bus from my
University back home and had disabled Google Drive syncing while on the bus
because for some reason, the software isn't smart enough to detect if there is
an active wifi connection before attempting a sync; this undoubtedly would kill
the battery. In my moments of reflection, I also remembered that I had
forgotten to reenable Google Drive sync when I had gotten home. This meant that
if there was some unreparable damage to my laptop, I would have lost a night's
worth of work. Not the worst thing in the world but still not ideal.

Still waiting, I wanted to see if I could be productive while at the Apple
store. I went on one of the laptops and tried to ssh into my school's
computers. Unfortunately, for some reason Apple blocks sshing over port 22 from
their store so I was stuck with nothing to do while I awaited the impending bad
news.

When the Apple employee returned, they showed some images they took of the
inside of the machine, saying that there was some sort of water damage that was
fresh. I knew this was impossible as there had only been one occasion where
water was spilt on my laptop around a year and a half ago at some hackathon. In
my state of shock, I accepted the news and realized that I had lost the laptop
I had used for the majority of my University life. This laptop contained all my
projects, several photos and countless documents, outlining my history for the
last 2 years.

After trying to recall all the documents I might have lost while on my way
home, I realized that my only true backup machine was in Waterloo. I realized
that this was the only way I could salvage the weekend and still be a bit
productive. This machine hadn't been touched in months, meaning that it did not
have all the tools I use for my workflow (including a pretty large migration
where I switched from vim to neovim). I had another laptop at home that ran
linux but after starting it up, I realized that there was NO good syncing
solution for Google Drive. Instantly regretted not using Dropbox, where they
actually care about developer facing platforms (and probably don't have
a broken syncing app to boot!).

Fortunately, in my state of disbelief, I held on to the hope that there might
still have been a change to boot into my laptop. One last time, I retired an
SMC reset and .... SUCCESS. My display turned on and as soon as I logged in,
I was able to start Google Drive and sync my once lost work.

This whole experience has left me with a bad taste in my mouth with Apple in
general. They did not perform ANY diagnostics on my laptop when they took it in
the back and instantly wrote it off. They also attempted to sell me new
hardware in the process. I had also been lied to by their support staff; they
mentioned the laptop having been "still moist" which made no sense as my laptop
hadn't been near water at all. Most importantly, it showed me how much Apple
didn't care about doing the proper dudiligence and took the easy explanation
out. Had they performed the proper diagnostics, I believe they could have
gotten my laptop working and saved hours of stress and aggravation.

## Lessons Learned
* Always make sure that you have a backup machine, that is at least somewhat
    configured in a way that you can start working if your primary dies.
* Make sure to have some machine you can ssh into that runs on port 80.
* Setup rsync nighlies so you have a local copy of your data
* Don't use backup solutions that only work on Windows and Mac (**cough**
    Google Drive **cough**)
* Don't Trust "Geniuses" :)

> Andrew
