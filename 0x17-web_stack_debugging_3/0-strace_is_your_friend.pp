# fixed php extensions in the wordpress file

exec { 'fix-file':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
 }
