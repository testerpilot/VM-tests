#!/bin/bash

iperf -n $1 -c 250Kb
iperf -n $1 -c 500Kb
iperf -n $1 -c 1Gb
iperf -n $1 -c 2Gb