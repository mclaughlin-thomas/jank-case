#!/bin/sh

wget 192.168.4.1/log.txt  # change this IP if the ESPkey IP doesn't match this for whatever reason

awk '{print $2}' log.txt > credentials.txt
