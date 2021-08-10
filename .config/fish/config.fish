if status is-interactive
  
    ### ADDING TO THE PATH ###
    
    # First line removes the path; second line sets it.  Without the first line,
    # your path gets massive and fish becomes very slow.
    set -e fish_user_paths
    set -U fish_user_paths $HOME/.local/bin $HOME/Applications $fish_user_paths
    
    ### EXPORT ###
    set fish_greeting                            # Supresses fish's intro message
    set TERM "alacritty"                         # Sets the terminal type
    set EDITOR "gedit"                           # $EDITOR use gedit in terminal
    
    
    ### ALIASES ###
    
    # spotify
    alias spotifymusic='LD_PRELOAD=/usr/local/lib/spotify-adblock.so spotify'

    # Git alias
    alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'


    # alias for extracting files
    alias extract="/bin/extract"

end
