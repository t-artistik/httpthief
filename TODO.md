# Introduction #

Httpthief was made as a proof of concept. The goal was to make this work, not to provide powerful framework which can be easily hacked. I don't plan to develop this project anymore.


# Details #

Some future goals:
  * httpthief.py ~~complete~~ partial refactoring (the code is still a mess).
  * cookie normalizer/parser
  * serve custom javascript file for clients
  * option to disable auth popup
  * cookie capture -> whole request capture
  * ~~1x1 white px image blob on HTTP 200~~ done, serving white BMP now.
  * option to send XHR instead IMG SRC
  * ~~option to prevent duplicating of records~~ done (no more credentials duplicating)
  * ~~option to store referer from clients http requests~~ done - stored in DB
  * dbname argument in DB class, to allow easily dbname modification (from command line)
  * command line / cli interface
  * better date format for storing timestamps in sqlite
  * remove hardcoded content
  * option to store whole client requests in sqlite.
  * documentation & examples
  * app needs more testing!