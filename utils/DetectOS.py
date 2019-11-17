#!/usr/bin/env python3
import distro

class DetectOS:
    def __init__(self):
        self.nomdist = distro.linux_distribution(full_distribution_name=False)
