# task1
import os
import json

pattern = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
with open('starter.json', 'w') as f_json:
    json.dump(pattern, f_json)
for root, folders in pattern.items():
    if os.path.exists(root):
        print(root, 'существует')
    else:
        for folder in folders:
            cur_dir = os.path.join(root, folder)
            os.makedirs(cur_dir)
