import requests
import argparse
from datetime import datetime, timedelta

parser = argparse.ArgumentParser(description="Turn DPRK IOCs to List", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--ip", action="store_true", help="Create a list of DPRK IPs")
parser.add_argument("--domain", action="store_true", help="Create a list of DPRK Domains")
parser.add_argument("--hash", action="store_true", help="Create a list of DPRK Hashes")
parser.add_argument("--delimiter", help="Specfify how list should separated", required=True)
args = parser.parse_args()

yesterday = datetime.now() - timedelta(1)
start = datetime.strftime(yesterday, '%Y-%m-%d')
end = datetime.now().strftime('%Y-%m-%d')
print(start)


if args.ip:
    url = "https://raw.githubusercontent.com/w00di/dprk/main/ips"
    response = requests.get(url)
    ioc_list = response.text
    ioc = ioc_list.split('\n')
    print(f'{args.delimiter}'.join(ioc))

elif args.domain:
    url = "https://raw.githubusercontent.com/w00di/dprk/main/domains"
    response = requests.get(url)
    ioc_list = response.text
    ioc = ioc_list.split('\n')
    ioc_split = f'{args.delimiter}'.join(ioc)
    print(f' hash_hunt {ioc_split} --start {start} --end {end}' )

elif args.hash:
    url = "https://raw.githubusercontent.com/w00di/dprk/main/hashes"
    response = requests.get(url)
    ioc_list = response.text
    ioc = ioc_list.split('\n')
    ioc_split = f'{args.delimiter}'.join(ioc)
    print(f' hash_hunt {ioc_split} --start {start} --end {end}' )