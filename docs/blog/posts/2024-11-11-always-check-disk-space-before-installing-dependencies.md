---
title: Always Check Disk Space Before Installing Dependencies
date: 2024-11-11
authors: [lifeadventurer]
categories:
  - DevOps
description: >
  A recent experience with server disk space and the importance of checking it before installing dependencies. Also, discovered the tool `ncdu` for managing disk usage.
---

# Always Check Disk Space Before Installing Dependencies!

Recently, I had a nerve-wracking experience with my server. I was in the middle
of installing some new dependencies when things suddenly went south. The
installation process was running smoothly—until it wasn’t. Without realizing it,
I’d maxed out my server’s disk usage. As a result, I couldn’t even SSH into the
server to see what went wrong or free up some space. Eventually, I had no choice
but to reboot the server to get back in.

This experience was a big reminder that disk space isn’t just something to keep
an eye on occasionally. It’s a **critical factor** to check _before_ installing
anything new on a server. Running out of disk space can cause unexpected
downtimes, prevent crucial services from running, and in some cases, even make
SSH inaccessible—as I learned the hard way.

On the bright side, I discovered a handy tool called `ncdu`! It's a **disk usage
analyzer** that makes it easy to visualize disk usage and pinpoint files or
directories hogging the most space. With `ncdu`, you can scan a directory and
quickly find unnecessary files or large logs to delete.

## Key Takeaways

1. **Always check disk usage** – Before installing dependencies or running any
   operations that might consume space, run a quick check on available disk
   space using commands like `df -h`, `du`, or `ncdu`.

2. **Monitor disk usage regularly** – Set up alerts or monitoring tools to
   notify you when disk usage reaches a critical level.

3. **Keep a buffer of free space** – Aim to keep a reasonable percentage of disk
   space free. This way, even if your application needs to expand temporarily,
   you’ll have room.

4. **Schedule maintenance** – Regularly remove unnecessary files, logs, and
   outdated dependencies to keep your server’s storage under control.

It’s easy to overlook disk space until it’s too late, but with these steps in
place, you can avoid disruptions and maintain smoother operations on your
server. A little proactive monitoring goes a long way!
