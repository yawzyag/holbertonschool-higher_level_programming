BB#!/bin/bash
# holi
curl -sD - "$1" | grep "Allow:" | cut -d" " -f2-
