"""
simple tool for tuning wifi signal access
"""
import re
import platform
import subprocess
from time import sleep
from typing import Callable

DEFAULT_DURATION_MS = 500
BEEP_DURATION_MULTIPLIER = 10
SLEEP_DURATION_S = 2
PING_COMMAND = 'ping www.seznam.cz -t'


def play_sound_windows(duration):
    winsound.Beep(440, duration)


def main(play_sound_func: Callable):
    p = subprocess.Popen(PING_COMMAND, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    for line in iter(p.stdout.readline, ''):
        line = line.decode(encoding='utf8')
        if line.startswith("Pinging "):
            continue
        if line.startswith("Ping request could not find host"):
            raise ValueError("Cannot find host")

        result = re.search(r'time=\d*', line)
        if result:
            time = int(result.group().replace("time=", "")) * BEEP_DURATION_MULTIPLIER
        else:
            time = DEFAULT_DURATION_MS
        print(f"{line}beep duration ({BEEP_DURATION_MULTIPLIER}x): {time}")
        play_sound_func(duration=time)
        sleep(SLEEP_DURATION_S)


if __name__ == "__main__":
    if platform.system() == "Windows":
        import winsound
        main(play_sound_func=play_sound_windows)
    else:
        raise NotImplementedError("TODO")
