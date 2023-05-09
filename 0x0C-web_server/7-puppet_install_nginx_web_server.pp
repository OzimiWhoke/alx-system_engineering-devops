# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}

# Define the Nginx virtual host configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
      listen 80;
      server_name _;
      
      location / {
        return 200 'Hello World!';
      }
      
      location /redirect_me {
        return 301 http://example.com/new_location;
      }
    }
  ",
  notify  => Service['nginx'],
}

# Enable the virtual host by creating a symbolic link
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

