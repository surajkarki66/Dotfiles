function spotifymusic --wraps='LD_PRELOAD=/usr/local/lib/spotify-adblock.so spotify' --description 'alias spotifymusic LD_PRELOAD=/usr/local/lib/spotify-adblock.so spotify'
  LD_PRELOAD=/usr/local/lib/spotify-adblock.so spotify $argv; 
end
