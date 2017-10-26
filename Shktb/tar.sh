#!/bin/bash

echo 'Starting to zip files...'

sleep 2

EXEC=zip
EXEC=unzip
FILES=*plag*dat
TBALL=plagDat
EXT=zip

DEST=/p/lscratchv/koneru2/2DShktb-up-mira/M192
DEST=${PWD}/$1

CASE=shktb
MAP=rflumap

FCOUNT=20
FMAX=20
FoCOUNT=14
FoMAX=23

while [ ${FoCOUNT} -le ${FoMAX} ]
do
	FCOUNT=20
	DIR=${DEST}/${1}_pf_small  #${FoCOUNT}
	while [ ${FCOUNT} -le ${FMAX} ]
	do
#		(cd ${DIR}/${FCOUNT} && ${EXEC} pf_$1_${FCOUNT}.${EXT} pf*)
		(cd ${DIR} && ${EXEC} pf_${FCOUNT}_${FoCOUNT}_1.${EXT} -d ${FCOUNT}_${FoCOUNT})
		echo 'Unzipped files in folder' $1'/'${FoCOUNT}_${FCOUNT}'...'

#		mv ${DIR}/${FCOUNT}/${TBALL}_$1_${FCOUNT}.${EXT} ${DEST}/M192_plagDat_master 
#		mv ${DIR}/${FCOUNT}/pf_$1_${FCOUNT}.${EXT} ${DEST}/M192_pf_master 
		sleep 2
	        ((FCOUNT=FCOUNT+10))
	done
#	sleep 2
	((FoCOUNT=FoCOUNT+1))
done 

echo 'All files are zipped in individual folders...'

#sleep 2

#FCOUNT=1
#FoCOUNT=19
#
#ZFILES=*zip
#TBALLF=plagDat_master
#
#while [ ${FoCOUNT} -le ${FoMAX} ]
#do
#	FCOUNT=1
#	DIR=${DEST}/${FoCOUNT}
#	(cd ${DIR} && ${EXEC} ${FoCOUNT}${TBALLF}.${EXT} \
#		         ${DIR}/${FCOUNT}/${ZFILES} && ((FCOUNT++)) \
#		      && ${DIR}/${FCOUNT}/${ZFILES} && ((FCOUNT++)) \
#		      && ${DIR}/${FCOUNT}/${ZFILES} && ((FCOUNT++)) \
#		      && ${DIR}/${FCOUNT}/${ZFILES} && ((FCOUNT++)) \
#		      && ${DIR}/${FCOUNT}/${ZFILES} && ((FCOUNT++)) )
#	echo 'Master zip file created at...'
##ls ${DEST}/1/${ZFILES}
#	ls ${DIR}/${ZFILES}
#	((FoCOUNT++))
#	sleep 2
#done
#sleep 5
#showq -i -u koneru2
