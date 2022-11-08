#!/bin/bash

DIR=/var/tmp/Backups/copiaCompleta
barra=/
if [ -d "$DIR" ] #SI NO HAY CARPETA DE COPIA COMPLETA LA CREARA Y HARÁ EL SALVADO DE HOY
then
barra=/
diaAntes=$(date --date="1 day ago" +%d-%m-%Y)
dirDiaAntes=/var/tmp/Backups/
dirDiaAntes="$dirDiaAntes$diaAntes"
dia=$( date +'%d-%m-%y')
dirT="$dir$dia"
echo "$dirT"
sudo mkdir $dirT
sudo rsync -av --link-dest=$dirDiaAntes ./Seguridad/ $dirT

else #HACER EL SALVADO DIARIO NORMAL CON LINK-DEST
'sudo mkdir /var/tmp/Backups/copiaCompleta'
'sudo rsync -av ./Seguridad/ /var/tmp/Backups/copiaCompleta/'
dir=/var/tmp/Backups/
barra=/
dia=$( date +'%d-%m-%y')
dirT="$dir$dia"
echo "$dirT"
sudo mkdir $dirT
dirT="$dirt$barra"
sudo rsync -av --compare-dest=/var/tmp/Backups/copiaCompleta/ ./Seguridad/ $dirT
fi
