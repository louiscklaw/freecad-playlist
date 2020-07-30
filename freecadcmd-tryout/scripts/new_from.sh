#!/usr/bin/env bash

set -ex


rsync -avzh ../$@/ .
