#install a flask package using pip3 in puppet
  package {'flask':
  ensure  => '2.1.0',
  provider  => 'pip3',
  name  => 'flask',
  }
