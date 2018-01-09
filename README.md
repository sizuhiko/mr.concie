# mr.concie

Custom SmartHome made by Google AIY

## Requirements

- Node.js (>= v6.11.5)
- Python (>= v3.6.1)
  - pip (>= v6.1)
  - pip-tools

## Platform Dependencies

Followings dependencies requires library depends each platform.
Please check and install the libraries.

- [snowboy](https://github.com/Kitt-AI/snowboy)
- [Google Assistant SDK](https://developers.google.com/assistant/sdk/guides/library/python/embed/setup)

## Install

### Install dependencies

```
# install snowboy
$ npm install
# install Google Assistant SDK
$ pip-sync
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
