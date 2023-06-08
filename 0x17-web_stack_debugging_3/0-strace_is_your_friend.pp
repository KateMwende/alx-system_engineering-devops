# replaced phpp with php in wordpress
exec { 'fix-error':
  command => "sed -i 's/phpp/php/' /var/www/html//wp-settings.php",
  path    => '/usr/local/bin/:/bin/'
}
