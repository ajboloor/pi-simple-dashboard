import json
import os
from subprocess import check_output

def disk_usage(path):
    "source: https://stackoverflow.com/questions/4260116/find-size-and-free-spa$
    """Return disk usage statistics about the given path.

    Will return the namedtuple with attributes: 'total', 'used' and 'free',
    which are the amount of total, used and free space, in bytes.
    """
    st = os.statvfs(path)
    free = st.f_bavail * st.f_frsize
    total = st.f_blocks * st.f_frsize
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    return round(float(free)/1024/1024/1024,2), round(float(used)/1024/1024/102$

data = json.load(open('data_test.json'))
with open("data_test.json", "r") as jsonFile:
    data = json.load(jsonFile)

tmp = data["device"]["name"]
data["device"]["name"] = "potato"

with open("data_test.json", "w") as jsonFile:
    json.dump(data, jsonFile)

device_name = os.system('uname -n')
storage_HDD = disk_usage('/mnt/serverhdd/')
storage_SD = disk_usage('/')
temp_internal = os.system('echo "scale=1; $(cat /sys/class/thermal/thermal_zone$
ram_free = float(check_output("cat /proc/meminfo | sed 's: ::g' |  grep -Po '(?$
ram_used = float(check_output("cat /proc/meminfo | sed 's: ::g' |  grep -Po '(?$
ram = (round(ram_free/1024,2), round(ram_used/1024,2))
print storage_HDD
print storage_SD
print ram
