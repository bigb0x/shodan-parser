import json
import argparse
import ipaddress

def extract_hosts(input_file, output_file):
    with open(input_file, 'r') as f, open(output_file, 'w') as out_f:
        for line in f:
            try:
                entry = json.loads(line)
                if 'http' in entry and 'host' in entry['http']:
                    host = entry['http']['host']
                    try:
                        ipaddress.ip_address(host)  # Check if the host value is an IP address
                        print(host)
                        out_f.write(host + '\n')
                    except ValueError:
                        # If it's not an IP address, assume it's a hostname
                        print(host)
                        out_f.write(host + '\n')
            except json.JSONDecodeError:
                # Skip lines that are not valid JSON objects
                continue

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract hosts from a JSON file.')
    parser.add_argument('-in', '--input', type=str, required=True, help='Input JSON file')
    parser.add_argument('-out', '--output', type=str, required=True, help='Output file')
    args = parser.parse_args()

    extract_hosts(args.input, args.output)