#!/bin/bash
echo "what is your name"
read name
echo "hello $name Welcome"
echo "today is $(date)"

mkdir -p /home/$USER/{$name}_dir

touch /home/$USER/{$name}_dir/welcome.txt

echo "welcome to your new folder, $name" > /home/$USER/{$name}_dir/welcome.text
