#!/bin/bash

result=$(timeout -k 50 45 python3 "./output_validator_measurements.py")

if [ -z "${result}" ]
then
        echo "{}"
else
        echo "$result"
fi




