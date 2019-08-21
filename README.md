# node-configure
Hack with the configure file for Node.js

[https://github.com/nodejs/node/blob/master/configure](https://github.com/nodejs/node/blob/master/configure) is a confusing little file that is half shell script and half Python code.  It operates in strange ways so it takes a while to grok it.

__configure__ also has funky interactions with Travis CI so this repo will let us understand how to modify __configure__ to support both Python 2 and Python 3.

See: [https://github.com/nodejs/node/issues/25789](https://github.com/nodejs/node/issues/25789)
