#!/bin/bash
DIR=/var/tmp/Backups/copiaCompleta
if [ -d "$DIR" ]
then
echo "El directorio copia existe"
else
'sudo mkdir /var/tmp/Backups/copiaCompleta'
'sudo rsync -av ./Seguridad/ /var/tmp/Backups/copiaCompleta/'
fi
dir=/var/tmp/Backups/
dia=$( date +'%d-%m-%y')
dirT="$dir$dia"
echo "$dirT"
sudo mkdir $dirT
barra=/
dirT="$dirt$barra"
sudo rsync -av --compare-dest=$dirT ./Seguridad/ /var/tmp/Backups/copiaCompleta
