# archeogit

`archeogit` is a Python utility to excavate a git repository in search of information.

## Installation

If you desire isolation of the environment onto which `archeogit`, and its dependencies are installed, setup and activate a virtual environment using `virtualenv --python=python3 .venv` and `. .venv/bin/activate`, respectively. Run `pip install -e .` or the included `./install.sh` to install `archeogit`.

## Configuration

The utility requires certain configuration settings to run. The file `configuration.template.json` provides a template for the configuration file. Make a copy of the `configuration.template.json` file and rename it to `configuration.json`. Edit `configuration.json` to add appropriate configuration settings.

The configuration file also has default settings for logging, which logs information level messages from the utility to console and file (`log.txt`).

## Usage

The command line interface to the utility provides the ability to excavate different types of information from the git repository. The type of information to excavate is specified as a subcommand to the main interface.

### Main Interface

```
$ archeogit --help
usage: archeogit [-h] [--config-file CONFIG_FILE] {blame} ...

Command line utility to excavate a git repository.

optional arguments:
  -h, --help            show this help message and exit
  --config-file CONFIG_FILE
                        Path to the configuration file. Default is
                        configuration.json.

Supported Commands:
  {blame}
    blame               Blame commits likely to have contributed a bug.
```

### Command: `blame`

```
$ archeogit blame --help
usage: archeogit blame [-h] [--csv] repository commit

positional arguments:
  repository  Path to a git repository that has been cloned locally.
  commit      SHA-1 of the commit known to have fixed the bug.

optional arguments:
  -h, --help  show this help message and exit
  --csv       Generate output in CSV format. If unspecified, the output is
              plaintext formatted suitable for human consumption.
```

#### Example

```
$ archeogit blame ~/repositories/ffmpeg/ b97a4b658814b2de8b9f2a3bce491c002d34de31
libavcodec/cbs_av1.c

| Contributor                              | Frequency |
| ---------------------------------------- | --------- |
| c8c81ac5026c20ce60860dc9aa905e5e1634bed1 |        22 |
2019-11-04 14:27:18,626 - archeogit - blame excavation took 0.83 seconds
```

```
$ archeogit blame ~/repositories/ffmpeg/ b97a4b658814b2de8b9f2a3bce491c002d34de31 --csv
commit,path,contributor,frequency
b97a4b658814b2de8b9f2a3bce491c002d34de31,libavcodec/cbs_av1.c,c8c81ac5026c20ce60860dc9aa905e5e1634bed1,22
2019-11-04 14:27:22,798 - archeogit - blame excavation took 0.82 seconds
```

## Environment

The application has been tested on an environment identified below.

  * Ubuntu 18.04.3 LTS
  * Python 3.7.2
  * virtualenv 16.4.0
