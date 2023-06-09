# this will fix the number of open files per second , for a process nginx

exec{'nginx-requests':
  path    => '/usr/local/bin/:/bin/',
  command => "sed -i /etc/default/nginx -e 's/15/4000/'"
}
exec{'restart-nginx':

  command => 'usr/sbin/service nginx restart',
  require => Exec['nginx-requests']

}
