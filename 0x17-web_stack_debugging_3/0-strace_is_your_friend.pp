# Fixes Apache 500 error

exec { 'fix-the 500 error in apache/ wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
}
