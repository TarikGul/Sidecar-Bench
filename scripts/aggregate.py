import os
import argparse

'''
Iterate through all the files in the chosen directory. 
'''
def scan_files(folder: str) -> dict:
    data = {}
    for root, dirs, files in os.walk(folder):
        for file in files:
            filename, extension = os.path.splitext(file)
            split_filename = filename.split('-')
            if extension == '.txt':
                parse_file(folder, file, data, split_filename[1])

    return data

'''
Parse the file, and organize it in a dictionary
I am using hardcoded key values here that abstract data directly from the .txt
files. Meaning, if any of the txt files structures change so does the way the function reads
the txt file. Basically the only thing that would need to change is the if else. 
'''
def parse_file(folder: str, filename: str, data: dict, version: str) -> None:
    f = open(folder + filename, 'r')

    version_data = {
        'Requests/sec': [],
        'Transfer/sec': [],
        'Completed': [],
        'Timeouts': [],
        'Failed': [],
        'Avg-Latency': [],
        'Min-Latency': [],
        'Max-Latency': [],
    }

    for line in f:
        split_line = line.split()
        if len(split_line) > 0:
            if split_line[0] == 'Requests/sec:':
                version_data['Requests/sec'].append(split_line[1])
            elif split_line[0] == 'Transfer/sec:':
                version_data['Transfer/sec'].append(split_line[1])
            elif split_line[0] == 'Total': # Completed Requests
                version_data['Completed'].append(split_line[3])
            elif split_line[0] == 'Failed':
                version_data['Failed'].append(split_line[2])
            elif split_line[0] == 'Timeouts':
                version_data['Timeouts:'].append(split_line[1])
            elif split_line[0] == 'Avg':
                version_data['Avg-Latency'].append(split_line[2])
            elif split_line[0] == 'Min':
                version_data['Min-Latency'].append(split_line[2])
            elif split_line[0] == 'Max':
                version_data['Max-Latency'].append(split_line[2])
            
    data[version] = version_data

'''
Inside aggregate_benchmarks, you can add any helper function that takes in
the data dictionary to which you can do any data analytics too and add any extra 
field to each version 
'''
def aggregate_benchmarks(data: dict) -> list:
    versions = []
    for key in data.keys():
        versions.append(key)

    versions.sort(key=lambda s: list(map(int, s[1:len(s)].split('.'))))

    '''
    Any actual data analytics can be done below now that the versions
    are sorted and all the important data is aggregated into its key
    value pairs 
    '''

    '''
    Add a performance key that will judge a version by its last version 
    '''
    performance(data, versions)

    return versions

def performance(data: dict, versions: list) -> None:
    prev_stable_version = ''

    for i in range(len(versions)):
        if i == 0:
            data[versions[i]]['performance'] = 'Earliest version, no data to compare too'
            prev_stable_version = versions[i]
        else:
            cur = data[versions[i]]
            prev = data[prev_stable_version]
            if is_stable(cur):
                avg_cur_latency = cur['Avg-Latency']
                avg_prev_latency = prev['Avg-Latency']
                cur_average = (float(avg_cur_latency[0][:-2]) + float(avg_cur_latency[1][:-2])) / 2
                prev_average = (float(avg_prev_latency[0][:-2]) + float(avg_prev_latency[1][:-2])) / 2
                # Calculate the increase or decrease in performance
                diff = cur_average - prev_average
                perf = round(((diff) / 100.0) * -1.0, 4)
                data[versions[i]]['performance'] = str(perf) + '%'
                # Set the new stable version to the current
                prev_stable_version = versions[i]
            else:
                continue
        
        print('version: ', versions[i] + ' ' + data[versions[i]]['performance'])

def is_stable(version_data: dict):
    bench1 = int(version_data['Failed'][0])
    bench2 = int(version_data['Failed'][1])
    if bench1 > 0 or bench2 > 0:
        return False
    else:
        return True

def write_file():
    print('do something')

def main():
    '''
    Parser
    '''
    parser = argparse.ArgumentParser()

    '''
    Data as a dictionary, with necessary key value pairs
    '''
    data = scan_files('./benchmarks/gcp-instance/')

    aggregate = aggregate_benchmarks(data)

if __name__ == "__main__":
    main()
