# coding=utf-8
"""
run shell
"""
__author__ = 'gucuijuan'
import os
import subprocess


def run_shell_by_subprocess(run_cmd):
    run_cmd = run_cmd.split(" ")
    popen = subprocess.Popen(run_cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    run_result = popen.stdout.readlines()
    popen.wait()
    return run_result


def run_shell_by_os(run_cmd):
    os.system(run_cmd)





