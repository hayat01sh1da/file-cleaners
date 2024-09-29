require_relative './src/application'

dirname, filename, mode, *_ = ARGV
puts 'Provide the directory which contains files you would like to delete'
dirname = gets.chomp

puts 'Provide the dirname or filename pattern you would like to delete'
pattern = gets.chomp

puts 'Provide -e(execution) if you would truly like to delete the files. This operation is cannot be undone, so trying to run without -e once is strongly recommended'
mode = gets.chomp

Application.run(dirname:, pattern:, mode:)
