# Script: 006_inline_python_code.rb
# Ruby Code

# Run inline Python code using Chef's `script` resource
script 'inline_python_code' do
  interpreter 'python' # Specify the Python interpreter
  code <<-EOH
import sys
print('Hello from Python', sys.version)
  EOH
end
