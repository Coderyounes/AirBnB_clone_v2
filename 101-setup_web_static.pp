package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>",
  require => File['/data/web_static/releases/test'],
}

file { ['/data/web_static/releases/test/', '/data/web_static/shared']:
  ensure => directory,
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  require => File['/data/web_static/releases/test'],
}

exec { 'chown_data_directory':
  command => 'chown -R ubuntu:ubuntu /data/',
  require => [File['/data/web_static/releases/test'], File['/data/web_static/shared']],
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => file('/etc/nginx/sites-available/default').content + "\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n",
  notify  => Service['nginx'],
}