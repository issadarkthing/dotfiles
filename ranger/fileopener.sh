#!/bin/bash

fpath=${1#file://}


if [[ -d $fpath ]]; then
	/usr/bin/alacritty -e "/usr/bin/ranger $fpath" &> /dev/null
else
	/usr/bin/alacritty -e "/usr/bin/ranger --selectfile=$fpath" &> /dev/null
fi
