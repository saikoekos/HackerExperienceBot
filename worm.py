HE = __import__("main")
from time import sleep
import re

def Worm(ips, clearLog, getSoftware, yourIp, hackedIps = []):
    HE.GetYourSoftware()
    hackedIps.append(HE.YourIp())
    for ip in ips:
        HE.ips.append(ip)

    while len(HE.ips) >= 1:
        HE.PrintDebug ("ips = " + str(HE.ips))
        ip = HE.ips[0]
        if ip in hackedIps:
            HE.ips.remove(ip)
        else:
            HE.ips.remove(ip)
            HE.Print("Starting worm on " + ip)
            if HE.Hack(ip, clearLog, getSoftware, getIps = True, getBTCs = True):
                program(ip, hackedIps)
            hackedIps.append(ip)

def program(ip, hackedIps):
    HE.PrintDebug("btcAddr " + str(HE.btcAddr))
    HE.PrintDebug("btcPass " + str(HE.btcPass))
    HE.PrintDebug("Ips to hack " + str(HE.ips))
    HE.PrintDebug("Hacked ips " + str(hackedIps))
    HE.Print("program started on " + ip)
    if HE.InternetUpload("Mikbrosim.vddos"):
        HE.InternetInstall("Mikbrosim.vddos", ip)


    """
    HE.PrintDebug(HE.yourSoftwares)
    HE.PrintDebug(HE.yourIds)
    HE.PrintDebug(HE.yourVersions)
    HE.PrintDebug(HE.yourSizes)
    HE.PrintDebug(HE.ids)
    HE.PrintDebug(HE.softwares)
    HE.PrintDebug(HE.versions)
    HE.PrintDebug(HE.sizes)
    """
