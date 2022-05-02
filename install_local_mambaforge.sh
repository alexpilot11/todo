#! /usr/bin/bash
# NOTE: INSTALL_DIR should be an absolute path

# if you source this file, it will set your conda environment for you
MAMBAFORGE_VERSION='4.10.1-4'
MAMBAFORGE_FILE=Mambaforge-${MAMBAFORGE_VERSION}-Linux-x86_64.sh
if [[ -z "$1" ]]
then
  INSTALL_DIR="${PWD}/mf"
else
  INSTALL_DIR="$1"
fi
if ! [[ -d ${INSTALL_DIR} ]]
then
  curl -L -O https://github.com/conda-forge/miniforge/releases/download/${MAMBAFORGE_VERSION}/${MAMBAFORGE_FILE}
  bash ./${MAMBAFORGE_FILE} -b -p ${INSTALL_DIR}
  rm ${MAMBAFORGE_FILE}
fi
