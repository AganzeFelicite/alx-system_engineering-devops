#end a running process
  exec { 'killmenow process':
  command  => '/bin/pkill killmenow',
  }
