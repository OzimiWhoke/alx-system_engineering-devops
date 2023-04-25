#!/usr/bin/env bash
#using Puppet to make changes to our configuration file

file { '/etc/ssh/ssh_config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('my_module/ssh_config.erb'),
}
