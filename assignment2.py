#!/usr/bin/env python3

"""
OPS445 Assignment 2 - Summer 2026
Program: assignment2.py
Author: Vidhiben Maheshbhai Patel

The Python code in this file is original work written by Vidhiben Patel.
No code in this file is copied from any source other than material provided
by the course instructor. I have not shared this Python script with anyone
except for submission for grading.

I understand that the Academic Honesty Policy will be enforced and that
violations will be reported and appropriate action will be taken.

Description:
This program displays Linux system and process memory usage using a
text-based bar graph. Milestone 1 converts a percentage into a graph and
reads the total and available system memory from /proc/meminfo.

Date: July 13, 2026
"""

import argparse
import os
import sys


def parse_command_args() -> object:
    """
    Set up and return the command-line arguments.

    The remaining command-line options will be completed during
    Milestone 2.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Memory Visualiser -- See Memory Usage Report with bar charts"
        ),
        epilog="Copyright 2023"
    )

    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=20,
        help="Specify the length of the graph. Default is 20."
    )

    # The human-readable -H option will be added in Milestone 2.

    parser.add_argument(
        "program",
        type=str,
        nargs="?",
        help=(
            "if a program is specified, show memory use of all associated "
            "processes. Show only total use if not."
        )
    )

    args = parser.parse_args()
    return args


def percent_to_graph(percent: float, length: int = 20) -> str:
    """
    Convert a decimal percentage into a bar graph.

    The percent argument should be between 0.0 and 1.0.
    The returned string contains hash symbols for the used portion
    and spaces for the unused portion.
    """
    # Scale the decimal percentage to the requested graph length.
    filled_length = round(percent * length)

    # Calculate the remaining portion of the graph.
    empty_length = length - filled_length

    # Join the filled and empty sections into one fixed-length string.
    graph = "#" * filled_length + " " * empty_length

    return graph


def get_sys_mem() -> int:
    """
    Return the total system memory in kilobytes.

    The total memory value is read from the MemTotal line inside
    the /proc/meminfo file.
    """
    # Open the Linux memory information file in read-only mode.
    with open("/proc/meminfo", "r") as meminfo:
        # Examine each line until the MemTotal entry is found.
        for line in meminfo:
            if line.startswith("MemTotal:"):
                # split() separates the label, number, and unit.
                # Index 1 contains the numeric memory amount.
                return int(line.split()[1])

    # Return zero if MemTotal cannot be found.
    return 0


def get_avail_mem() -> int:
    """
    Return the currently available system memory in kilobytes.

    The available memory value is read from the MemAvailable line
    inside the /proc/meminfo file.
    """
    # Open the Linux memory information file in read-only mode.
    with open("/proc/meminfo", "r") as meminfo:
        # Examine each line until the MemAvailable entry is found.
        for line in meminfo:
            if line.startswith("MemAvailable:"):
                # Index 1 contains the numeric memory amount.
                return int(line.split()[1])

    # Return zero if MemAvailable cannot be found.
    return 0


def pids_of_prog(app_name: str) -> list:
    """
    Return all process IDs associated with an application.

    This function will be completed during Milestone 2.
    """
    pass


def rss_mem_of_pid(proc_id: str) -> int:
    """
    Return the resident memory used by a process.

    This function will be completed during Milestone 2.
    """
    pass


def bytes_to_human_r(kibibytes: int, decimal_places: int = 2) -> str:
    """
    Convert a kibibyte value into a human-readable binary unit.

    This instructor-provided function will be used during the final
    submission for output such as MiB and GiB.
    """
    # Binary suffixes are based on divisions of 1024.
    suffixes = ["KiB", "MiB", "GiB", "TiB", "PiB"]

    suffix_index = 0
    result = kibibytes

    # Divide by 1024 until the value fits an appropriate unit.
    while result > 1024 and suffix_index < len(suffixes) - 1:
        result /= 1024
        suffix_index += 1

    # Format the result with the requested number of decimal places.
    return f"{result:.{decimal_places}f} {suffixes[suffix_index]}"


if __name__ == "__main__":
    # Read the user's command-line options and positional argument.
    args = parse_command_args()

    if not args.program:
        # Read total and currently available memory.
        total_memory = get_sys_mem()
        available_memory = get_avail_mem()

        # Memory in use equals total memory minus available memory.
        used_memory = total_memory - available_memory

        # Avoid dividing by zero if total memory could not be read.
        if total_memory > 0:
            used_percent = used_memory / total_memory
        else:
            used_percent = 0

        # Create the bar graph using the selected graph length.
        graph = percent_to_graph(used_percent, args.length)

        # Display the memory label, graph, percentage, used memory,
        # and total memory in aligned output.
        print(
            f"{'Memory':<15}"
            f"[{graph}| {used_percent:.0%}] "
            f"{used_memory}/{total_memory}"
        )

    else:
        # Program-specific memory reporting is completed in Milestone 2.
        pass
