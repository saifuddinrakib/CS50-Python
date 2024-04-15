from typing import Self


class Vault:
    def __init__ (self, galleons=0, sickles=0, knuts=0):
        self.galleons=galleons
        self.sickles=sickles
        self.knuts=knuts

    def __str__(self):
    return (f"{Self.galleons} Galleons, {Self.sickles} Sickles, {Self.knuts} Knuts")



