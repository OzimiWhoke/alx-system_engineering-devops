#!/usr/bin/env bash
#  creating a custom HTTP header response, but with Puppet.
# The name of the custom HTTP header must be X-Served-By
# The value of the custom HTTP header must be the hostname of the server Nginx is running on

class { 'nginx':
  add_default_headers => false,
}

nginx::resource::server { 'default':
  listen_port => 80,
  server_name => '_',
  location    => {
    'proxy_pass'           => 'http://localhost:8080/',
    'proxy_set_header'     => 'X-Served-By $hostname',
    'proxy_set_header'     => 'Host $host',
    'proxy_set_header'     => 'X-Real-IP $remote_addr',
    'proxy_set_header'     => 'X-Forwarded-For $proxy_add_x_forwarded_for',
    'proxy_connect_timeout'=> '600s',
    'proxy_send_timeout'   => '600s',
    'proxy_read_timeout'   => '600s',
  }
}
