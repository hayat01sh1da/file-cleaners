require_relative './src/application'

puts 'Provide the directory which contains files you would like to delete'
dirname = gets.chomp

puts 'Provide the dirname or filename pattern you would like to delete'
pattern = gets.chomp

puts 'Provide d(dry_run: default) to make sure what directories and files are to be delete first. Then, provide e(execution) if you would truly like to delete the files. This operation is cannot be undone, so be alert to your operation!'
mode = gets.chomp

params = { dirname:, pattern:, mode: }.reject { |_, value| value.empty? }

Application.run(**params)
