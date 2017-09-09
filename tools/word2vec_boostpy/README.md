# word2vec_boostpython for Mac

word2vec binding for Python using Boost.Python

Its goal: good wrapper to easily handle vectors which were created by word2vec.
For example, `get_vectors` returns Numpy's ndarray.

Original C implementation: https://code.google.com/p/word2vec/

Code License: Apache License 2.0 (same to original project)

# Build on Mac
Check out paths in setup.py
```
sudo python setup.py install
```

If you use other OS, install boost and fix path in setup.py.

[Original word2vec_boostpython.README.md](./word2vec_boostpython.README.md)