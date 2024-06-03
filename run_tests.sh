#!/bin/bash

if ! [ -d "website_diff_examples" ]; then
    git clone https://github.com/trevorcampbell/website_diff_examples.git
fi

examples_dir="website_diff_examples/examples"

rm -rf $examples_dir/temp
rm -rf $examples_dir/*/diff
rm -rf $examples_dir/*/*/prerendered
mkdir $examples_dir/temp
cp -rf $examples_dir/* $examples_dir/temp

for dir in $examples_dir/*; do [ -d "$dir" ] && [ "$dir" != "$examples_dir/temp" ] && website_diff --old $dir/old/ --new $dir/new/ --diff $dir/diff/; done

cp -rf $examples_dir/temp/* $examples_dir
rm -rf $examples_dir/temp