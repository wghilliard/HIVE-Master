import os
import requests
import time
import sys
import json

FCL_PATH = '/data/docker_user/fcl_files'

FCL_PATH = '/Users/wghilliard/data/fcl_files'

MASTER_IP = 'localhost'


def start(events):
    for item in os.listdir(FCL_PATH):
        if item[:2] == 'MC':
            time.sleep(1)
            print item[:-4]
            tmp = item[:-4]
            tmp_list = tmp.split("_")

            if len(tmp_list) > 3:
                name = "_".join(tmp_list[2:4])
            else:
                name = tmp_list[2]

            data_dir = {"name": name, 'new_file': "fcl_files/{0}".format(item),
                        "events": events, "start": False, "out_dir": "{0}/".format(name)}

            # print data_dir
            # print "<url>" +         'http://{0}:5000/api/jobs'.format(MASTER_IP)
            encoded_data = json.dumps(data_dir)
            request = requests.post('http://{0}:5000/api/jobs'.format(MASTER_IP), encoded_data)
            # print request.reason


if __name__ == "__main__":
    # start(sys.argv[1])
    start(100)
