# increase f8le limit for holberton user


exec {' increase soft':
command => "/bin/sed -i 's/holberton soft nofile 5/holberton soft nofile 5000/' /etc/security/limits.conf",
}

exec {' increase hard':
command => "/bin/sed -i 's/holberton hard nofile 4/holberton hard nofile 4000/' /etc/security/limits.conf",
}
