#!/usr/bin/env bash

# styles.css

for file in .hotreload main.js manifest.json;
do
  ls $file
  cp $file ~/Documents/obsidian-vaults/TestVault/.obsidian/plugins/obsidian-experiments-plugin
done
