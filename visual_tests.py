#!/usr/bin/env python
"""
plays several tests to localhost for testing.

"bunny" clip created by:

ffmpeg -ss 00:00:30 -i BigBuckBunny_DivX_HD720p_ASP.divx -t 7 -vf scale=-2:240 -c:v libx264 -c:a aac bunny.avi
"""
from pathlib import Path
import subprocess

R = Path(__file__).parent

VIDPATH = R / 'tests'
IMGPATH = R / 'doc'
HOST = 'localhost'
STATIC = IMGPATH / 'logo.png'
MOVING = VIDPATH / 'cc_land.gif'
VIDEO = VIDPATH / 'bunny.avi'

print('these tests enable a user to visually confirm the code is working.')
print('the streaming is just on your own computer.')
print('press   q   in the terminal window to proceed to the next test.')

# %% Microphone
print('PyLivestream splash with live microphone audio')
subprocess.check_call(['python', 'MicrophoneLivestream.py', '-y',  HOST, '-image', STATIC],
                      cwd=R)

print('1990s vector graphics with live microphone audio')
subprocess.check_call(['python', 'MicrophoneLivestream.py', '-y',  HOST, '-image', MOVING],
                      cwd=R)
# %% Webcam
print('Webcam test')
subprocess.check_call(['python', 'WebcamLivestream.py', '-y', HOST],
                      cwd=R)
# %%  Music
print('PyLivestream splash with orchestra music  (caption)')
subprocess.check_call(['python', 'FileGlobLivestream.py', '-y',  HOST, '-image', STATIC,
                       'tests', 'orch.ogg'],
                      cwd=R)

print('1990s vector graphics with orchestra music (NO caption')
subprocess.check_call(['python', 'FileGlobLivestream.py', '-y',  HOST, '-image', MOVING,
                       'tests', 'orch.ogg'],
                      cwd=R)
# video
print('Looping video')
subprocess.check_call(['python', 'FileGlobLivestream.py', '-y', HOST, VIDPATH, VIDEO.name],
                      cwd=R)
# %% Screenshare
print('Screenshare + microphone')
subprocess.check_call(['python', 'ScreenshareLivestream.py', '-y',  HOST],
                      cwd=R)
# %% loop video
print('Looping video')
subprocess.check_call(['python', 'FileLoopLivestream.py', '-y',  VIDEO, HOST],
                      cwd=R)
