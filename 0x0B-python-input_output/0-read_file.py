#!/usr/bin/python3
"""Defines read_file a text file-reading function."""


def read_file(file=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(file, encoding="utf-8") as f:
        print(f.read(), end="")
