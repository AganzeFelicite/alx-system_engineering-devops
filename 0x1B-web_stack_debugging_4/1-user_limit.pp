# the problem of high number of files open fixed

exec{'replacing':
  provider => shell,
  command  => "sudo sed -i 's/nofile 5/nofile 500000/' /etc/security/limits.conf",
  before   => Exec['replacing-1st'],

}
exec{'replacing-1st':
provider => shell,
command  => "sudo sed -i 's/nofile 4/nofile 40000/' /etc/security/limits.conf",
}

