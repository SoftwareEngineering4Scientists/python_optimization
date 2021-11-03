#!/bin/bash

alias gnutime="/home/jovyan/.conda/envs/swefs/bin/time -f '%e\t%M'"

gnutime python extender.py 1000
