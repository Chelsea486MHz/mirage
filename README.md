# 🏝️ MIRAGE
Real-time anonymizer for video calls

Literally less than 100 lines of Python it's not that big a deal

## Description

`mirage` is a privacy tool used to anonymize real-time video recordings of a person through face scrambling.

You can still be identified by metadata like background light fluctuations, but `mirage` ensures that face recognition is maximally disrupted.

## Use cases

- anyone who wants their face scrambled on camera

## How it works

`mirage` opens the specified video capture device and renders in real time a GUI element that can be captured by software like [OBS](https://obsproject.com/)

The rendered video displayed a scrambled version of the user's face using random noise.

## Usage

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python3 ./mirage.py
```

## Installation
```
$ git clone https://github.com/Chelsea486MHz/mirage
$ cd mirage
$  python mirage.py VIDEO_DEVICE
```