# httpthief #

**httpthief** is a standalone http server written in python. It serves metacontent to exploit browser and web application weakness. Main features are:


  1. Sending HTTP basic auth request to the user.
  1. Gathering provided credentials and optional data in URL.


This script is intended to exploit Cross Site Scripting (XSS) flaws in badly written web applications. By injecting own HTML code to such an application, you are able to force victim's browser to send a request to an attacker web server, resulting in cookie hijack. Moreover it is possible to trick the user with fake password popup, which looks much like a legit one. Captured data is stored in Sqlite database.


The goal is to provide preconfigured, stright-forward and multiplatform environment.


**This is only a proof of concept. I don't take any responsibility for illegal usage.**

## Requirements ##

  * Python interpreter >= 2.5
  * sqlite3 python module