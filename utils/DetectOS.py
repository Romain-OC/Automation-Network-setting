#!/usr/bin/env python3
import distro

class DetectOS:
    #function that request the distribution name
    def __init__(self):
        self.nomdist = distro.linux_distribution(full_distribution_name=False)
