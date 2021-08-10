# Lines configured by zsh-newuser-install

#------------------------------
# History stuff
#------------------------------
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000


#------------------------------
# Variables
#------------------------------
# Compilation flags
export ARCHFLAGS="-arch x86_64"

# Node
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm

# Editor
export EDITOR="gedit"

# If you come from bash you might have to change your $PATH.
export PATH=$HOME/bin:/usr/local/bin:$PATH


#-----------------------------
# Dircolors
#-----------------------------
LS_COLORS='rs=0:di=01;34:ln=01;36:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:su=37;41:sg=30;43:tw=30;42:ow=34;42:st=37;44:ex=01;32:';
export LS_COLORS


#------------------------------
# Keybindings
#------------------------------
bindkey -v
typeset -g -A key
bindkey '^?' backward-delete-char
bindkey '^[[5~' up-line-or-history
bindkey '^[[3~' delete-char
bindkey '^[[6~' down-line-or-history
bindkey '^[[A' up-line-or-search
bindkey '^[[D' backward-char
bindkey '^[[B' down-line-or-search
bindkey '^[[C' forward-char 
bindkey "^[[H" beginning-of-line
bindkey "^[[F" end-of-line


#------------------------------
# Alias stuff
#------------------------------

# ncmpcpp
alias music='ncmpcpp'

# spotify
alias spotifymusic='LD_PRELOAD=/usr/local/lib/spotify-adblock.so spotify'

# Git alias
alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'


# alias for extracting files
alias extract="/bin/extract"


#------------------------------
# Comp stuff
#------------------------------

autoload -Uz compinit
compinit
# End of lines added by compinstall

zstyle :compinstall filename '/home/surajkarki/.zshrc'


#------------------------------
# Prompt
#------------------------------

autoload -Uz promptinit
promptinit

# Enable colors and change prompt:

# Starship
eval "$(starship init zsh)"


#------------------------------
# Plugins stuff
#------------------------------

source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/.zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh



