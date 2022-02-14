import ctypes
import sys
import time
from datetime import datetime as dt

blocked_sites = ['www.facebook.com', 'facebook.com',
                 'www.youtube.com', 'youtube.com',
                 'www.gmail.com', 'gmail.com',
                 'www.anichart.net', 'anichart.net']

Window_host = r"C:\Windows\System32\drivers\etc\hosts"
default_hoster = Window_host
redirect = "127.0.0.1"


def block_websites(start_hour, end_hour):
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, start_hour) < dt.now() < dt(dt.now().year, dt.now().month,
                                                                                       dt.now().day, end_hour):
            print("Do you work you slacker")
        with open(default_hoster, "wt") as hostfile:
            hosts = hostfile.read()
            for site in blocked_sites:
                if site not in hosts:
                    hostfile.write(redirect + ' ' + site + '\n')
    else:
        with open(default_hoster, 'rt') as hostfile:
            hosts = hostfile.readline()
            hostfile.seek(0)
            for host in hosts:
                if not any(site in host for site in blocked_sites):
                    hostfile.write(host)
            hostfile.truncate()
        print("Enjoy your respite")
    time.sleep(3)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    block_websites(9, 19)
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
