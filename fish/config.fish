

function zp

	# if argument given, use that as query
	if test ! -z $1 ; then
		local zpath=`z | awk '{print $2}' | fzf --preview='ls {}' -q $1`
	else
		local zpath=`z | awk '{print $2}' | fzf --preview='ls {}'`
	end

	# cd into path if not empty string
	# otherwise zsh will cd into home dir if empty string
	[[ ! -z $zpath ]] && cd $zpath

end
