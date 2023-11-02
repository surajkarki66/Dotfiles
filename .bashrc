#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias ytaudio="yt-dlp -f 'ba' -x --no-playlist"
PS1='[\u@\h \W]\$ '
JUPYTERLAB_DIR=$HOME/.local/share/jupyter/lab
alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'
