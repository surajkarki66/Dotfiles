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
eval "$(/home/surajkarki/anaconda3/bin/conda shell.bash hook)"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/surajkarki/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/surajkarki/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/surajkarki/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/surajkarki/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion


export PATH="/home/surajkarki/.detaspace/bin:$PATH"

# The next line updates PATH for the Google Cloud SDK.
if [ -f '/home/surajkarki/Downloads/google-cloud-sdk/path.bash.inc' ]; then . '/home/surajkarki/Downloads/google-cloud-sdk/path.bash.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/home/surajkarki/Downloads/google-cloud-sdk/completion.bash.inc' ]; then . '/home/surajkarki/Downloads/google-cloud-sdk/completion.bash.inc'; fi
export CHROME_EXECUTABLE=/usr/bin/google-chrome-stable
#SDK exporting - this will solve your issue
export ANDROID_HOME=/home/surajkarki/Android/Sdk 

#Tools exporting - it can be need in your case
export PATH=/home/surajkarki/Android/Sdk/platform-tools:$PATH
export PATH=/home/surajkarki/Android/Sdk/tools:$PATH
export PATH=/home/surajkarki/Android/ndk-build:$PATH


