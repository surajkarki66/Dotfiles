from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy

# Import the function that move the window to the next and prev group
from functions import Functions
# Import default mod keys
from keys.default import *


class Keybindings:
    def __init__(self):
        self.mod = MOD
        self.alt = ALT
        self.altgr = ALTGR
        self.terminal = TERMINAL
        self.shift = SHIFT
        self.control = CONTROL

        # All keys are stored keys
        self.keys = []

    def init_keys(self):
        #################### CUSTOM KEYS  ##########################
        return [
            ############   BINDINGS FOR MONADTALL   ##############
            Key([self.mod], "h", lazy.layout.left()),
            Key([self.mod], "l", lazy.layout.right()),
            Key([self.mod], "j", lazy.layout.down()),
            Key([self.mod], "k", lazy.layout.up()),
            Key([self.mod, "shift"], "h", lazy.layout.swap_left()),
            Key([self.mod, "shift"], "l", lazy.layout.swap_right()),
            Key([self.mod, "shift"], "j", lazy.layout.shuffle_down()),
            Key([self.mod, "shift"], "k", lazy.layout.shuffle_up()),
            Key([self.mod], "i", lazy.layout.grow()),
            Key([self.mod], "m", lazy.layout.shrink()),
            Key([self.mod], "n", lazy.layout.normalize()),
            Key([self.mod], "o", lazy.layout.maximize()),
            Key([self.mod, "shift"], "space", lazy.layout.flip()),

            ############   BINDINGS FOR FLOATING   ##############
            Key([self.mod, "shift"], "g", lazy.window.toggle_floating(),
                desc='toggle floating'),
            Key([self.mod, "shift"], "f", lazy.window.toggle_fullscreen(),
                desc='toggle fullscreen'),

            # Move screen to next and previous workspace
            Key([self.mod], "k", lazy.screen.next_group(),
                desc="Move screen to the next workspace"),
            Key([self.mod], "j", lazy.screen.prev_group(),
                desc="Move screen to the previous workspace"),

            # Move window to next group
            Key([self.control, self.shift], "k", Functions.window_to_next_group(),
                desc="Move screen to the next workspace"),
            Key([self.control, self.shift], "j", Functions.window_to_prev_group(),
                desc="Move screen to the previous workspace"),
            # Kill Functions
            Key([self.mod, self.altgr], "c", Functions.kill_all_windows_minus_current(),
                desc="Kill all windows except current in the workspace"),
            Key([self.mod, self.altgr], "x", Functions.kill_all_windows(),
                desc="Kill all windows except current in the workspace"),

            # Toggle between different layouts as defined below
            Key([self.mod], "Tab", lazy.next_layout(),
                desc="Toggle between layouts"),


            # Basic Commands
            Key([self.mod], "q", lazy.window.kill(),
                desc="Kill focused window"),
            Key([self.mod], "Return", lazy.spawn(
                self.terminal), desc="Launch terminal"),
            Key([self.mod, "shift"], "r",
                lazy.restart(), desc="Restart qtile"),
            Key([self.mod, "shift"], "q",
                lazy.shutdown(), desc="Shutdown qtile"),
            Key([self.mod], "r", lazy.spawn('rofi -modi system:/home/surajkarki/.config/rofi/scripts/powermenu.sh -show system -theme dmenu -icon-theme "Papirus-Dark" -show-icons'),
                desc="Run Rofi"),
            Key([self.mod], "d", lazy.spawn('dmenu_run'), desc="Run dmenu"),


            # Applications hotkeys
            # Most apps are opened with Super + left self.alt keys
            Key([self.mod, self.alt], "e", lazy.spawn(
                "emacs"), desc="Open Doom Emacs"),
            Key([self.mod, self.alt], "l", lazy.spawn(
                "librewolf"), desc="Open Librewolf"),
            Key([self.mod, self.alt], "v", lazy.spawn(
                "codium"), desc="Open VS codium"),
            Key([self.mod, self.alt], "a", lazy.spawn("pavucontrol"),
                desc="Open Pulse audio GUI controller"),
            Key([self.mod, self.alt], "s", lazy.spawn(
                "signal-desktop"), desc="Open Signal"),
            Key([self.mod, self.alt], "d", lazy.spawn(
                "discord"
            ), desc="Open Discord"),
            Key([self.mod, self.alt], "n", lazy.spawn(
                "pcmanfm"
            ), desc="Open PCManFM file browser"),
            Key([self.mod, self.alt], "i", lazy.spawn(
                "insomnia"
            ), desc="Open Insomnia"),
            Key([self.mod, self.alt], "r", lazy.spawn(
                self.terminal + " ranger"
            ), desc="Open Ranger file manager"),
            Key([self.mod], "s", lazy.spawn(
                "spotifymusic"), desc="Open Spotify"),
            Key([self.mod], "p", lazy.spawn(
                "passmenu"
            ), desc="Open passmenu"),


            # Media hotkeys
            Key([self.mod], 'Up', lazy.spawn('pulseaudio-ctl up 5')),
            Key([self.mod], 'Down', lazy.spawn('pulseaudio-ctl down 5')),
            Key([], "XF86AudioPlay", lazy.spawn(
                'playerctl play-pause')),
            Key([], "XF86AudioPause", lazy.spawn(
                'playerctl play-pause')),

            # Screenshots
            Key([], "Print", lazy.spawn('xfce4-screenshooter')),
            Key([self.alt], "Print", lazy.spawn('xfce4-screenshooter -f -c')),
            Key([self.shift], "Print", lazy.spawncmd(
                "xfce4-screenshooter -f -s /home/daniel/Pictures/Screenshots/")),

            # ------------ Hardware Configs ------------

            # Volume
            Key([], "XF86AudioLowerVolume", lazy.spawn(
                "pactl set-sink-volume @DEFAULT_SINK@ -5%")),
            Key([], "XF86AudioRaiseVolume", lazy.spawn(
                "pactl set-sink-volume @DEFAULT_SINK@ +5%")),
            Key([], "XF86AudioMute", lazy.spawn(
                "pactl set-sink-mute @DEFAULT_SINK@ toggle")),

            # Brightness
            Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
            Key([], "XF86MonBrightnessDown",
                lazy.spawn("brightnessctl set 10%-")),
        ]

    def init_keys_groups(self, group_names):
        """
        Create bindings to move between groups
        """
        keys = []
        for i, icon in enumerate(group_names, 1):
            keys += [Key([self.mod], str(i), lazy.group[icon].toscreen()), Key(
                [self.mod, 'shift'], str(i), lazy.window.togroup(icon, switch_group=True))]

        return keys


class Mouse:
    def __init__(self):
        self.mod = MOD

    def init_mouse(self):
        mouse = [
            Drag([self.mod], "Button1", lazy.window.set_position_floating(),
                 start=lazy.window.get_position()),
            Drag([self.mod], "Button3", lazy.window.set_size_floating(),
                 start=lazy.window.get_size()),
            Click([self.mod], "Button2", lazy.window.bring_to_front())
        ]
        return mouse
