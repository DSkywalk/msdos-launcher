# MSDOS-Launcher

A simple Steam Play compatibility tool to run any **Non-Steam** MSDOS games using native Linux DOSBox.

### 1. Add Non-Steam Game
![Add Non-Steam Game](https://github.com/user-attachments/assets/88a8fa53-388f-4b52-ac41-bdba84aa96d3)

### 2. Select DOSBox Launcher
![imagen](https://github.com/user-attachments/assets/a7af85cc-53db-4e53-bb79-e4182ad4f123)

![imagen](https://github.com/user-attachments/assets/1cb7ad2f-767b-4a4f-a1d0-4e75d243852a)

_This is a simple fork project of [Boxtron](https://github.com/dreamer/boxtron), a great option for official MSDOS Steam games._


## Features

* Launch your games with great Steam features.
* Configuration per game or use your defaults.
* Steam Overlay working out of the box (required [**dosbox-staging**](https://github.com/dreamer/dosbox-staging))


## Installation (manual)

You'll need to install dependencies manually and then proceed to installation steps:
- [tarball (single-user)](#installation-using-tarball-for-a-single-user)
- [source (system-wide)](#installation-from-source-system-wide)


### Dependencies

You will need Python (>= 3.5), DOSBox (>= 0.74), inotify-tools, TiMidity++,
and a soundfont.  Optionally, you can use FluidSynth as well.

##### Fedora

    $ sudo dnf install dosbox inotify-tools timidity++ fluid-soundfont-gm

##### OpenSUSE

    $ sudo zypper install dosbox inotify-tools timidity fluid-soundfont

##### Debian, Ubuntu, Mint, Pop!\_OS

    $ sudo apt install dosbox inotify-tools timidity fluid-soundfont-gm

##### Arch, Manjaro

    $ sudo pacman -S dosbox inotify-tools timidity++ soundfont-fluid

##### NixOS

    $ nix-env -f '<nixpkgs>' -iA dosbox inotify-tools timidity soundfont-fluid


### Installation (using tarball, for a single user)

1. Download and unpack tarball to `compatibilitytools.d` directory (create one if it does not exist):

       $ cd ~/.local/share/Steam/compatibilitytools.d/ || cd ~/.steam/root/compatibilitytools.d/
       $ curl -L https://github.com/DSkywalk/msdos-launcher/releases/download/v0.2.0/msdos-launcher.tar.xz | tar xJf -

2. Start/restart Steam.
3. In game properties window select "Force the use of a specific Steam Play
   compatibility tool" and select "DOSBox Launcher (native MSDOS)".


### Installation (from source, system-wide)

This installation method is explained in detail in [the packaging guide](PACKAGING.md).

1. Clone the repository and install the script system-wide:

       $ git clone https://github.com/DSkywalk/msdos-launcher.git
       $ cd msdos-launcher
       $ sudo make install

2. Start/restart Steam.
3. In game properties window select "Force the use of a specific Steam Play
   compatibility tool" and select "DOSBox Launcher (native MSDOS)".


## Configuration

As **LAUNCH OPTIONS** you can set `MSDOS_CREATE_CONFIG=1` to create an empty config file
to customize your DOSBox behaviour for this game.

![Added launch option](https://github.com/user-attachments/assets/4be20502-5542-4773-9607-25cbfa6120b9)

Launch your game and in your game folder a **hash-config** file should appear.
Now [Configure DOSBox](https://www.dosbox-staging.org/getting-started/introduction/) as you wish and you can remove `MSDOS_CREATE_CONFIG=1` from your LAUNCH OPTIONS.

⚠️ Do not change the name of the **hash-config** file and if in a while you change the game path your **hash-config** file name _may_ change too.

## Known issues

As of January 2020 you might encounter one of the following bugs:

- Some games experience random KeyUp events in fullscreen.
  It's a [DOSBox bug](https://www.vogons.org/viewtopic.php?f=31&t=66491), use
  [**dosbox-staging**](https://github.com/dreamer/dosbox-staging) to avoid it.
- Alt+Tab does not work in fullscreen. It's a DOSBox bug, use
  [**dosbox-staging**](https://github.com/dreamer/dosbox-staging) to avoid it.
- Modern game controllers might not work at all. It's a DOSBox bug, use
  [**dosbox-staging**](https://github.com/dreamer/dosbox-staging) to avoid it.
- Steam Overlay causes visual glitch. This was a DOSBox bug - use DOSBox 0.74-3 or
  [**dosbox-staging**](https://github.com/dreamer/dosbox-staging) to avoid it.
- Mouse cursor issues in Gnome 3.30. This was a Gnome issue, fixed in 3.32.
