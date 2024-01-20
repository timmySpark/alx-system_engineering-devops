# Using Puppet, install flask from pip3.

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# installing Werkzeug too , requires flask 
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['Flask'],
}

