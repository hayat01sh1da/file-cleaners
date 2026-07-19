# frozen_string_literal: true
# rbs_inline: enabled

require 'optparse'
require_relative 'version'
require_relative 'application'

module SpreenClean
  # Command line interface behind the `file-clean` executable:
  # `file-clean [PATTERN] [--dirname DIR] [--mode d|e]`.
  class CLI
    MODES = %w[d e].freeze #: Array[String]

    # @rbs argv: Array[String]
    # @rbs return: Integer
    def self.start(argv = ARGV)
      new(argv).run
    end

    # @rbs argv: Array[String]
    # @rbs return: void
    def initialize(argv)
      @argv    = argv.dup
      @dirname = '.'
      @mode    = 'd'
      @action  = :clean_files
    end

    # @rbs return: Integer
    def run
      parser.parse!(argv)
      __send__(action)
    rescue Application::InvalidModeError, OptionParser::ParseError => e
      warn e.message
      1
    end

    private

    attr_reader :argv #: Array[String]
    attr_reader :dirname #: String
    attr_reader :mode #: String
    attr_reader :action #: Symbol

    # @rbs return: Integer
    def clean_files
      Application.run(dirname:, pattern:, mode:)
      0
    end

    # @rbs return: Integer
    def print_version
      puts VERSION
      0
    end

    # @rbs return: Integer
    def print_help
      puts parser
      0
    end

    # @rbs return: String
    def pattern
      argv.shift || '*'
    end

    # @rbs return: OptionParser
    def parser
      @parser ||= OptionParser.new('Usage: file-clean [PATTERN] [options]') do |opt|
        opt.on('--dirname DIR', 'Directory tree to clean (default: .)') { |value| @dirname = value }
        opt.on('--mode MODE', MODES,
               "Operation mode (#{MODES.join(' or ')}; d = dry run, e = execute, default: d)") { |value| @mode = value }
        opt.on('--version', 'Print the version') { @action = :print_version }
        opt.on('-h', '--help', 'Print this help') { @action = :print_help }
      end
    end
  end
end
