#!/usr/bin/env bash

set -ex

cd freecadcmd-tryout/take-screen-shot

  rm -rf screencapture/*.jpg

  freecadcmd ./helloworld.py
  freecad ./take_screenshot.py -l test.log

  ls -l screencapture/test-screenshot0.jpg

cd ../..
