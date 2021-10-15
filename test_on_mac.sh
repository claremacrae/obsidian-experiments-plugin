#!/usr/bin/env bash

for file in .hotreload main.js manifest.json styles.css;
do
  ls $file
  cp $file ~/Documents/obsidian-vaults/TestVault/.obsidian/plugins/obsidian-experiments-plugin
done
