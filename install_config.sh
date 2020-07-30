#!/bin/bash

config_path=~/.config/nvim/
config_file=${config_path}init.vim
old_config_file=${config_path}init_old.vim

function copy_old_file {
    # Copy old config file
    if test -f "$config_file"; then
        cp $config_file $old_config_file
        echo "Old config file copied: ${old_config_file}"
    fi
}


function install_new_config {
    # Install new config file
    cp init.vim $config_file
    echo "New config file installed: ${config_file}"
}

copy_old_file
install_new_config

