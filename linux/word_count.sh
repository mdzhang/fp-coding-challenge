#!/usr/bin/env bash

tr -s '[:space:]' |         # compress whitespace chars
tr -d '[:punct:]' |         # remove punctuation
tr ' ' '\n' |               # replace spaces with newlines
sort |                      # sort lines
uniq -c                     # count number of times a line occurs
