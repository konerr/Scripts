#!/bin/bash

echo 'Creating directories...'

sleep 2

DEST=${PWD}
EXEC=/home/rahul.koneru/codes/repos/CCMT-Nek5k/Nek5000/bin
CASE=so
SCRIPT=job.slurm

NMIN=200
NMAX=800
PMIN=4
PMAX=16
FILE=rprof300001
while [ ${PMIN} -le ${PMAX} ]
do
	NMIN=200
	while [ ${NMIN} -le ${NMAX} ]
	do
	
	cd ${DEST}
        mkdir N${NMIN}_p${PMIN}
	DIR=${DEST}/N${NMIN}_p${PMIN}
#	echo ${DIR}
	mkdir ${DIR}/profiles
	scp rahul.koneru@hpg2.rc.ufl.edu:/ufrc/bala/rahul.koneru/NekExamples/so_ALL/convergence_AV/N${NMIN}_p${PMIN}/profiles/${FILE} ${DIR}/profiles

#	echo $(bc <<<"scale=5; 10/${NMIN}")
#	echo $(( PMIN+1 ))
#	echo $(( (PMIN+1)*3/2 ))

	echo 'Edited' 'N'${NMIN}'_p'${PMIN}'...'

	((NMIN=NMIN*2))

	sleep 2
	done
	((PMIN=PMIN*2))
done
echo 'All changes are done...'
#sleep 5
#showq -i -u koneru2
