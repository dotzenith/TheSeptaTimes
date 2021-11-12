#!/bin/bash

rm -rf build && rm -rf dist

python3 -m build --sdist --wheel . && twine upload dist/* 
