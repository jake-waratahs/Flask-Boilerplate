#!/bin/bash
# Script for running on a CI Server
cd WebApp

# Use the sample config if one doesn't exist in the project
if [ ! -f WebApp/Application/config/variables.py ]
	then
	cp WebApp/Application/config/variables.py.example WebApp/Application/config/variables.py
fi

make test
rm -rf WebApp/Application/config/variables.py