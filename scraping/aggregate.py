#!/usr/bin/env python

import os
import json
import sys

files = [os.path.join(sys.argv[1], x) for x in os.listdir(sys.argv[1])]
files = [x for x in files if os.path.isfile(x)]

data = []

for p in files:
    with open(p) as f:
        data.append(json.loads(f.read()))

print(json.dumps(data, ensure_ascii=False))