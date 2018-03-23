import json
import os
from subprocess import check_output
from apscheduler.schedulers.blocking import BlockingScheduler
import psutil

kB_to_GB = 1 / float(1024 * 1024 * 1024);
KB_to_GB = 1 / float(1024 * 1024);
MB_to_GB = 1 / float(1024);

data = {}
data["device"] = {}
data["temperature"] = {}
data["storage"] = {}
data["storage"]["SD"] = {}
data["storage"]["HDD"] = {}
data["RAM"] = {}
data["cpu"] = {}

def disk_usage(path):
    """source: https://stackoverflow.com/questions/4260116/find-size-and-free-spa
    Return disk usage statistics about the given path.
    """
    st = os.statvfs(path)
    free = st.f_bavail * st.f_frsize
    total = st.f_blocks * st.f_frsize
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    total = round(float(total * kB_to_GB), 2)
    free = round(float(free * kB_to_GB), 2)
    used = round(float(used * kB_to_GB), 2)
    return used, free

def cpu_usage():
    cpu_usages = []
    psutil.cpu_times_percent(interval=0.0);
    for cpu in psutil.cpu_percent(interval=0.1,percpu=True):
	cpu_usages.append(cpu);
    return cpu_usages

def ram_usage():
    ram_free = float(check_output("cat /proc/meminfo | sed 's: ::g' |  grep -Po '(?<=MemFree:).*' | grep -Po '.*(?=kB)'",shell=True))
    ram_used = float(check_output("cat /proc/meminfo | sed 's: ::g' |  grep -Po '(?<=MemAvailable:).*' | grep -Po '.*(?=kB)'",shell=True))
    ram_free = round(ram_free * MB_to_GB, 2)
    ram_used = round(ram_used * MB_to_GB, 2)
    return ram_used, ram_free

def internet_check():
    import requests
    try:
        response = requests.get("http://www.google.com")
        status = "Online"
    except requests.ConnectionError:
        status = "Offline"
    return status

#data = json.load(open('data_test.json'))
#with open("data_test.json", "r") as jsonFile:
#    data = json.load(jsonFile)
#
#tmp = data["device"]["name"]
#data["device"]["name"] = "potato"
#
#with open("data_test.json", "w") as jsonFile:
#    json.dump(data, jsonFile)

def fetch_data():
    device_name = check_output("echo -n $(uname -n)", shell=True)
    device_OS = check_output("echo -n $(cat /etc/*-release | grep -Po '(?<=PRETTY_NAME=).*')", shell=True)
    device_internet = internet_check()
    device_uptime = check_output("echo -n $(uptime -p | grep -Po '(?<=up ).*')", shell=True)
    storage_HDD = disk_usage('/mnt/serverhdd/')
    storage_SD = disk_usage('/')
    temp_internal = round(float(check_output("cat /sys/class/thermal/thermal_zone0/temp", shell=True))/1000,2)
    temp_external = float(25.0)
    ram = ram_usage()
    cpu = cpu_usage()

    data["device"]["name"] = str(device_name)
    data["device"]["OS"] = str(device_OS)[1:len(device_OS)-1]
    data["device"]["internet"] = str(device_internet)
    data["device"]["uptime"] = str(device_uptime)
    data["temperature"]["internal"] = temp_internal
    data["temperature"]["external"] = temp_external
    data["storage"]["SD"]["used"] = storage_SD[0]
    data["storage"]["SD"]["avail"] = storage_SD[1]
    data["storage"]["HDD"]["used"] = storage_HDD[0]
    data["storage"]["HDD"]["avail"] = storage_HDD[1]
    data["RAM"]["used"] = ram[0]
    data["RAM"]["avail"] = ram[1]
    data["cpu"]["core1"] = cpu[0]
    data["cpu"]["core2"] = cpu[1]
    data["cpu"]["core3"] = cpu[2]
    data["cpu"]["core4"] = cpu[3]

#    print data
    print(str(device_name))
    print(str(device_OS[1:len(device_OS)-1]))
    print(str(device_internet))
    print(str(device_uptime))
    print(str(temp_internal))
    print(str(storage_HDD))
    print(str(storage_SD))
    print(str(ram))
    print(str(cpu))

if __name__ == "__main__":
    fetch_data()
    with open('data_test.json', 'w') as outfile:
	json.dump(data, outfile)	
#scheduler = BlockingScheduler()
#scheduler.add_job(fetch_data(), 'interval', hours=1)
#scheduler.start()
