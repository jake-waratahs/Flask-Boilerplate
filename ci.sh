#!/bin/bash
# Script for running on a CI Server
cd WebApp

# Use the sample config if one doesn't exist in the project
if [ ! -f Application/config/variables.py ]
	then
	cp Application/config/variables.py.example Application/config/variables.py
fi

make test &&
rm -rf Application/config/variables.py