# Ensure the web root directory has the correct permissions
file { '/path/to/your/webroot':
  ensure => directory,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}

# Ensure Apache is running
service { 'apache2':
  ensure => running,
  enable => true,
}

# Ensure required PHP modules are installed
package { ['php', 'libapache2-mod-php', 'php-mysql']:
  ensure => installed,
}