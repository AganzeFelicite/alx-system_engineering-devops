#end a running process
  exec { 'killing it':
  command  => '/bin/pkill killlmenow',
  }
