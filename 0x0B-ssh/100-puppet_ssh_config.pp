#remove ssh login with ssh
  exec {'Turn off passwd auth process':
  path    => '/bin',
  command => 'echo "  PasswordAuthentication no" >> /etc/ssh/ssh_config',

  }
  exec {'Declare identity file process':
  path    => '/bin',
  command => 'echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  }
