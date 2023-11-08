# webstack debighing 3

exec { 'remove extra p':
command => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
