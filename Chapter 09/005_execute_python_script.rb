# Script: 005_execute_python_script.rb
# Ruby Code

# Execute a Python script using Chef's `execute` resource
execute 'run_python_script' do
  command 'python /path/to/script.py' # Replace with the actual path to your Python script
  action :run
end
