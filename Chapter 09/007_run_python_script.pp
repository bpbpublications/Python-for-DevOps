# Script: 007_run_python_script.pp

# Puppet exec resource to run a Python script
exec { 'run_python_script':
  command => '/usr/bin/python /path/to/script.py', # Replace with the actual path to your Python script
  path    => ['/usr/bin', '/usr/sbin'],           # Set the PATH environment
}
