#!/usr/bin/env bash

zip -r xfajku06-SYN SYN-doc.pdf app syn.py
zip -d xfajku06-SYN.zip __MACOSX/\*
zip -d xfajku06-SYN.zip \*/.DS_Store
#zip -d -r xfajku06-SYN.zip `unzip -l xfajku06-SYN.zip | grep -e "app/.*__pycache__" | rev | cut -d ' ' -f -1 | rev`
#unzip