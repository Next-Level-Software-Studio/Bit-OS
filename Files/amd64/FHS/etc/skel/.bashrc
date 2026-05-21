#Interactive and non-interactive
HISTSIZE=0
HISTCONTROL=ignorespace


# Interative mode only
[[ $- != *i* ]] && return
[ -f /etc/bash/bashrc ] && . /etc/bash/bashrc
PS1="\[\e[1;30m\]┌── \[\e[0m\]\[\e[1;36m\]\t, \$(date +%d/%m/%Y)\[\e[0m\] \[\e[1;30m\]|\[\e[0m\] \[\e[1;32m\]\u@\h\[\e[0m\]: \[\e[1;33m\]\w\[\e[0m\] \n\[\e[1;30m\]|\[\e[0m\]\n\[\e[1;30m\]└─> \[\e[0m\]"
echo '  ____   _  _              ___   ____'
echo ' | __ ) (_)| |_           / _ \ / ___|'
echo ' |  _ \ | || __|  _____  | | | |\___ \'
echo ' | |_) || || |_  |_____| | |_| | ___) |'
echo ' |____/ |_| \__|          \___/ |____/'

#add your fun stuff bellow