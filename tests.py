# -*- coding: utf-8 -*-
import json

data = []
with open("groups.txt") as f:
    for line in f:
        print(type(json.loads(line)))

