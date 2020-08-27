#!/usr/bin/env bash

set -ex

rm -rf screencapture/*.jpg

freecadcmd ./helloworld.py
freecad ./take_screenshot.py -l test.log