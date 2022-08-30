import subprocess


def putty(ip):
    try:
        pid = subprocess.Popen("putty.exe " + ip).pid
    except TypeError:
        pass

