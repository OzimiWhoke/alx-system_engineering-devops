# Using strace, find out why Apache is returning a 500 error using puppet

exec { 'fix-apache-error':
  command => '/path/to/fix-command',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
