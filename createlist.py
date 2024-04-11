import requests
import argparse

parser = argparse.ArgumentParser(description="Turn DPRK IOCs to List", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--ip", action="store_true", help="Create a list of DPRK IPs")
parser.add_argument("--domain", action="store_true", help="Create a list of DPRK Domains")
parser.add_argument("--hash", action="store_true", help="Create a list of DPRK Hashes")
parser.add_argument("--delimiter", help="Specfify how list should separated", required=True)
args = parser.parse_args()

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
    print(f'{args.delimiter}'.join(ioc))

elif args.hash:
    url = "https://raw.githubusercontent.com/w00di/dprk/main/hashes"
    response = requests.get(url)
    ioc_list = response.text
    ioc = ioc_list.split('\n')
    print(f'{args.delimiter}'.join(ioc))