# mr.concie

Custom SmartHome made by Google AIY

## Requirements

- Node.js (>= v6.11.5)
- Python (>= v3.6.1)
  - pip (>= v6.1)
  - pip-tools

### Raspberry Pi 3

Please see [Installing Python 3.6 on Raspbian](https://gist.github.com/dschep/24aa61672a2092246eaca2824400d37f) if you use Raspberry Pi 3.

## Platform Dependencies

Followings dependencies requires library depends each platform.
Please check and install the libraries.

- [snowboy](https://github.com/Kitt-AI/snowboy)
  - install npm
  - [Install Dependencies](https://github.com/Kitt-AI/snowboy#dependencies)
- Google Assistant SDK
  - [Set Up Hardware and Network Access](https://developers.google.com/assistant/sdk/guides/library/python/embed/setup)
  - [Configure and Test the Audio](https://developers.google.com/assistant/sdk/guides/library/python/embed/audio)
  - [Configure a Developer Project and Account Settings](https://developers.google.com/assistant/sdk/guides/library/python/embed/config-dev-project-and-account)

### Raspberry Pi 3

#### pygame requirements

```
$ sudo apt-get install libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev
$ sudo apt-get install libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev
```

## Install

### Install application dependencies

```
# install snowboy
$ npm install
# install Google Assistant SDK
$ pip install -r requirements.txt
```

### Compile Snowboy Python3 Wrapper

```
$ cd node_modules/snowboy/swig/Python3

# Please change line #5 of Makefile if you use Ubuntu/Raspberry Pi/Pine64/Nvidia Jetson TX1/Nvidia Jetson TX2
# #SWIG := swig
# SWIG := swig3.0

$ make
```

### Generate credentials

Check [Generate credentials](https://developers.google.com/assistant/sdk/guides/library/python/embed/install-sample#generate_credentials) page.
`Authorization tool` has installed by `install application dependencies`.
Only use `google-oauthlib-tool`, can generate credentials.

### Register the Device Model

[Register the Device Model](https://developers.google.com/assistant/sdk/guides/library/python/embed/register-device)

### Register the Device

Register device to your project.
In the following command, replace `my-model` with your registered.

```
# Raspberry Pi
$ UUID=$(cat /proc/sys/kernel/random/uuid)
# Mac OSX
$ UUID=$(uuidgen)

$ googlesamples-assistant-devicetool register-device --device $UUID --model 'my-model' --client-type SDK_SERVICE
```

You can check all the device created under your developer project at any time by using the command below:

```
$ googlesamples-assistant-devicetool list --device

Device Instance Id: cdb0bcba-eb9c-11e7-a920-dca9049065c5
    Model: my-light
```

### Generate your HOTWORD

Generate your HOTWORD for starting your google assistant app. 
HOTWORD can generate with [snowboy HOTWORD DETECTION](https://snowboy.kitt.ai/).
Generate and download your HOTWORD, rename to `hotword.pmdl` and put to the app root.

### Environment

Copy `.env.sample` to `.env`, and edit configurations followings.

- `ASSISTANT_APP_NAME` Your Google Assistant Application name
- `TTS_LANG` Speak interaction response from your assistant app by the Language
- `ASSISTANT_LANGUAGE_CODE` Google Assistant Application interaction language
- `ASSISTANT_APP_INTERACTION` Interaction keyword depends your language
- `DEVICE_ID` Your Device ID
- `DEVICE_MODEL_ID` Your Device Model ID

## Run

```
$ python main.py
```

Please say your HOTWORD like a `OK, Google`.
Enjoy !

## Troubleshooting

### Error about Compile a Python Wrapper on Mac OSX

```
$ make
clang++ -I../../ -O3 -fPIC -D_GLIBCXX_USE_CXX11_ABI=0  -bundle -flat_namespace -undefined suppress snowboy-detect-swig.o \
	../..//lib/osx/libsnowboy-detect.a -L/Users/home/.pyenv/versions/3.6.4/lib/python3.6/config-3.6m-darwin -lpython3.6m -ldl -framework CoreFoundation -Wl,-stack_size,1000000 -framework CoreFoundation -lm -ldl -framework Accelerate -o _snowboydetect.so
ld: -stack_size option can only be used when linking a main executable
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make: *** [_snowboydetect.so] Error 1
```

It remove `,-stack_size,1000000` and run compile manually.

```
$ clang++ -I../../ -O3 -fPIC -D_GLIBCXX_USE_CXX11_ABI=0  -bundle -flat_namespace -undefined suppress snowboy-detect-swig.o \
../..//lib/osx/libsnowboy-detect.a -L/Users/home/.pyenv/versions/3.6.4/lib/python3.6/config-3.6m-darwin -lpython3.6m -ldl -framework CoreFoundation -Wl -framework CoreFoundation -lm -ldl -framework Accelerate -o _snowboydetect.so
```

Maybe generated `_snowboydetect.so`.
