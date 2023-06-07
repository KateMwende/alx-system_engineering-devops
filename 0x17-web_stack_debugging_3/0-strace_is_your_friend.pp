# fixed php extensions in the wordpress file

file { '/var/www/html/wp-settings.php':
  ensure  => 'file',
  content => file('/var/www/html/wp-settings.php').content.gsub('phpp', 'php'),
}
