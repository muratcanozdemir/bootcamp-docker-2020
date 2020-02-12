#!/bin/sh

# Use supervisor to keeps Jupyter notebook running.
# This will automatically reset notebook when a user hits Quit.

jupyter_home="${HOME}/.jupyter"

if [ ! -d "$jupyter_home" ];then
    mkdir -p "$jupyter_home"
fi

if [ ! -d "${HOME}/notebooks" ];then
    mkdir -p "${HOME}/notebooks"
fi

service supervisor start
exit 0
