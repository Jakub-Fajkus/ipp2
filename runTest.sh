#!/usr/bin/env bash

rm ./*.!!!
rm ./*.err

cd diagram
bash _stud_tests.sh && php5.6 test.php

