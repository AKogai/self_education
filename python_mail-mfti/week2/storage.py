import os
import tempfile
import json
import argparse

# storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
# with open(storage_path, 'w') as f:
#     print('3', file=f)
#     f.close()

# parser = argparse.ArgumentParser())
# parser.add_argument('s')
# args = parser.parse_args()
# with open("data_file.json", "w") as write_file:
#         json.dump(args.s, write_file)

parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')

    args = parser.parse_args()
with open("data_file.json", "w") as write_file:
         json.dump(args.--key, write_file)