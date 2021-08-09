#!/bin/bash

cd ui
ng build --prod=true --aot=true
cd .. 
rm -rf static/*
cp -r ui/dist/ui/* static/

docker build -t agenda .