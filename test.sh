#!/usr/bin/env bash

set -ex

# # echo "helloworld"
# sudo add-apt-repository -y ppa:freecad-maintainers/freecad-stable
# sudo apt-get update
# sudo apt-get install -y freecad freecad-python3


# sudo mkdir -p /usr/lib/freecad-python3/Mod

# # install freecad mod
# git clone https://github.com/JMG1/ExplodedAssembly $HOME/.FreeCAD/Mod/ExplodedAssembly


# freecad open file test
for i in $(ls -1 *.FCStd); do python3 ./.travis/freecad_open_test.py $i; done

# for i in $(ls -1 *.FCStd); do ls -l $i; done
