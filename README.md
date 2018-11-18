# `lutris-bulk.adder.py`

## Description

This is a simple Python script to import a directory of ROM files into Lutris.  The directory must contain only games from one platform.  I have only tested this on my own computer for a limited number of platforms.

I don't really know what will happen if Lutris is open during the import, so make sure to restart Lutris immediately after importing, or close it before the import - this script will write directly to Lutris's SQLite database, so proceed with caution.

## Requirements

- `PyYAML`

## Usage

### Required arguments

`-d` / `--directory`: Directory to scan for ROM files.
`-r` / `--runner`: Slug name of Lutris runner to use (e.g. `dolphin`, `snes9x`)
`-p` / `--platform`: Platform name.  A list of platform names is included in the script, but if one is not included, you can figure it out by looking at the Lutris [runner class definitions](https://github.com/lutris/lutris/tree/master/lutris/runners) for the value(s) listed under the `platforms` member.

### Lutris path arguments

These default to the default locations that Lutris will install to.

`-ld` / `--lutris-database`: Path to the Lutris SQLite database.  Default: `~/.local/share/lutris/pga.db`
`-ly` / `--lutris-yml-dir`: Directory containing Lutris installed game YAML files.  Default: `~/.config/lutris/games`
`-lg` / `--lutris-game-dir`: Lutris games installation directory.  This shouldn't do anything as ROMs aren't installed, but the Lutris database needs it.  Default: `~/Games`

### Other arguments

`-f` / `--file-types`: Space-separated list of file types to scan for.  Defaults to `iso,zip,sfc,gba,gbc,gb,md,n64,nes,32x,gg,sms`
`-o` / `--game-options`: Additional options to write to the YAML file under the "game" key (e.g. platform number as required for Dolphin)
`-s` / `--strip-filename`: Space-separated list of strings to strip from filenames when generating game names.
`-n` / `--no-write`: Do not write YML files or alter Lutris database, only print data to be written out to stdout. (i.e. dry run)

### Example

`./lutris-bulk-adder.py -d /data/Emulation/Wii -r dolphin -s '(USA)' -p "Nintendo Wii" -o platform=1`

Adds all files in `/data/Emulation/Wii` to the `dolphin` runner, ignoring substrings containing `(USA)` in the filename when deriving the game name, for the `Nintendo Wii` platform, and adds `platform: '1'` to the `game` key in the YAML file.