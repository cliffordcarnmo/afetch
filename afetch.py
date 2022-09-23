#!/usr/bin/python

import subprocess

info = {
    "host": "cat /proc/sys/kernel/hostname",
    "os": "cat /etc/os-release | grep PRETTY_NAME | cut -d\'\"\' -f 2",
    "kernel": "(uname -rmo; echo ', '; cat /proc/modules | uniq | wc -l; echo ' modules')",
    "uptime": "uptime -p",
    "processes": "(ps ax | wc -l; echo ', '; cat /proc/loadavg | cut -d' ' -f1,2,3; echo ' load average')",
    "packages": "pacman -Q | wc -l",
    "shell": "echo $SHELL",
    "cpu": "(cat /proc/cpuinfo | grep 'model name' | uniq | cut -d':' -f2 | xargs; echo ', '; cat /proc/cpuinfo | grep 'cpu cores' | uniq | cut -d: -f2 | xargs; echo ' cores')",
    "gpu": "lspci | grep -i vga | cut -d':' -f3 | xargs",
    "mem": "(free --mega | grep Mem | cut -d':' -f2 | xargs | cut -d' ' -f2; echo ' MB / '; free --mega | grep Mem | cut -d':' -f2 | xargs | cut -d' ' -f1; echo ' MB, ';cat /proc/meminfo | grep Dirty | cut -d':' -f 2 | xargs; echo ' dirty')"
}

for i in info:
    print("\033[1;35m" + i + "\033[0m: " + subprocess.run(info[i],shell=True,capture_output=True,text=True).stdout.replace('\n',''))

