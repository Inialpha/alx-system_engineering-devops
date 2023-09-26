#configure web server
include stdlib

package { 'nginx':
}

exec {'install nginx':
command  => 'apt -y update; apt -y install nginx',
provider => shell,
}

file { '/var/www/html/index.html':
ensure  => 'present',
content => 'Hello World!',
require => Exec['install nginx'],
}

$new_string="\tserver_name _;\n\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;"

file_line { 'replace':
ensure => 'present',
match  => 'server_name _;$',
line   => $new_string,
path   => '/etc/nginx/sites-enabled/default',
}

exec {'run':
command  => 'sudo service nginx restart',
provider => shell,
}
