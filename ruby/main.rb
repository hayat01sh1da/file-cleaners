require_relative './src/application'

dirname, filename, mode, *_ = ARGV
Application.run(dirname:, filename:, mode:)
