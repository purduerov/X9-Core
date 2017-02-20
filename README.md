# X9-Core
All of X9's core software for the 2016-2017 Purdue ROV team.

## Scotty:
scotty is our favorite [cheif engineer](http://www.ex-astris-scientia.org/inconsistencies/movies/underwater-scotty-stid.jpg) that install the dependencies, runs the software, and runs tests.

### Using Scotty to Install Dependencies:
```
scotty install [--pi] [--dev [--cam]]
   Installs required files. Autodetects install type
   --pi:     Install as if this is a Pi
   --dev:    Install as if this is a dev machine
   --cam:    Also install mjpg streamer for dev
 ```
 `sudo ./scotty install` will auto detect if you're on a Raspberry Pi or not, and install all the needed items. This includes:
 - `pip`
 - `install/requirements.txt` and `install/requirements-hw.txt`
 - `mjpg-streamer`
 - configure I2C

If you aren't on a Raspberry Pi, it will not install the hardware items or mjpg streamer. If auto detect fails, you can pass in `--pi` or `--dev`. If you're installing on dev machine and want mjpg streamer, pass in `--cam`.

Installs should be idempotent, which means you can rerun them with no adverse effects. If requirements ever get updated, just rerun the install. 

Note: `sudo` is needed, because some dependencies need to be installed via `apt-get`

### Running the App:
```
scotty run [--rov] [--debug]
   Runs the full ROV stack
   --rov:    Just test the ROV main loop
   --debug:  Set FLASK_DEBUG and ROV_DEBUG
```
If you want to run the full ROV program, run `./scotty run`. This starts the flask application. If you want to just test the ROV main loop, run `./scotty run --rov`. This starts the rov for tests, without the flask app. Passing in `--debug` sets the environmental variables configured in `environment.debug` in `install/config.json`. By default, it will set the `FLASK_DEBUG` to true, as well as `ROV_DEBUG`, which can be used to optionally turn things on and off in debug:
```python
if os.environ['ROV_DEBUG']
    print "This only prints with --debug!"
```

### Shell/Virtualenv:
```
scotty shell [--debug]
   Runs a new shell, with the activated venv. Exit to leave venv
   --debug:  Set FLASK_DEBUG and ROV_DEBUG
```
`./scotty shell` will start a new version of your current shell, with the appropriate environmental variables set. This lets you run `flask run`, and `mjpg_streamer`, as they will be added to your paths. The virtualenv is also added to your path, so dependencies will be installed there. If you pass in `--debug`, the `environment.debug` variables in `install/config.json` will be set as well.

### Test:
```
scotty test [files...] [--pep8] [--pylint]
   Runs the full testing framework
   files:    optional list of files to test
   --pep8:   Run pep8 test
   --pylint: Run pylint test
```
Scotty will run linting tests to check for things like unused variables, bad imports, bad spacing, etc. Think of it like a compiler. This helps to catch errors that will not show up until runtime. Right now there are two tests:
- pep8: tests against [pep8 style guide](https://www.python.org/dev/peps/pep-0008/)
- pylint: tests for undeclared variables, bad whitespace, misspelled items

Will hope to add more tests that can test our modules individually

### To install node and Vue:
1. `curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -`

2. `sudo apt-get install nodejs`

3. now, navigate to `X9-Core/frontend/` and run `npm install`

4. once that's done, just run `npm run build` to condense the files for the webpage
