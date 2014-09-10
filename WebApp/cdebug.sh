#!/bin/sh

./util/compile.sh ./Application/static/css/
./util/regenerate.sh ./Application/models Model
./util/regenerate.sh ./Application/views View
python run.py --debug $@

