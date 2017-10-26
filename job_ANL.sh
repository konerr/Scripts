#!/bin/sh
# Job submission script for ANL machines

WALL_TIME=720
NODES=128
PROCS=128
MODE=script
MAIL=rahul.koneru@ufl.edu
CASE=shktb
NAME=2Dshktb-22-1-small
OUTPUT=run.log
PROJECT=SoPE_2
EXEC=/home/koneru/Rocflu_shktb_May2616/Rocflu/rflump

qsub -t $WALL_TIME -n $NODES --proccount $PROCS --jobname $NAME -o $OUTPUT -A $PROJECT -M $MAIL $EXEC -c $CASE -v 2
