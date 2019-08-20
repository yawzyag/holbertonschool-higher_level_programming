B#!/bin/bash
# holi
curl -sD - $1 | grep "Content-Length" | cut -d" " -f2
