# frozen_string_literal: true
# rbs_inline: enabled

require 'optparse'
require_relative 'version'
require_relative 'application'

module SpreenClean
  # Command line interface behind the `file-clean` executable:
  # `file-clean [PATTERN] [--dirname DIR] [--mode d|e] [--yes]`.
  class CLI
    MODES = %w[d e].freeze #: Array[String]
    # The execution mode asks for confirmation above this many matches.
    BULK_DELETE_THRESHOLD = 100 #: Integer

    # @rbs argv: Array[String]
    # @rbs return: Integer
    def self.start(argv = ARGV)
      new(argv).run
    end

    # @rbs argv: Array[String]
    # @rbs return: void
    def initialize(argv)
      @argv              = argv.dup
      @dirname           = '.'
      @mode              = 'd'
      @skip_confirmation = false
      @action            = :clean_files
    end

    # @rbs return: Integer
    def run
      parser.parse!(argv)
      __send__(action)
    rescue Application::InvalidModeError, Application::RootDirnameError, OptionParser::ParseError => e
      warn e.message
      1
    end

    private

    attr_reader :argv #: Array[String]
    attr_reader :dirname #: String
    attr_reader :mode #: String
    attr_reader :skip_confirmation #: bool
    attr_reader :action #: Symbol

    # @rbs return: Integer
    def clean_files
      application = Application.new(dirname:, pattern:, mode:)
      application.validate_mode!
      application.validate_dirname!
      unless confirmed?(application)
        warn 'Aborted the execution mode without deleting anything.'
        return 1
      end

      application.run
      0
    end

    # Guards the execution mode against oversized sweeps: above
    # BULK_DELETE_THRESHOLD matches it asks for an explicit `y`, unless
    # `--yes` was given for scripted use.
    # @rbs application: Application
    # @rbs return: bool
    def confirmed?(application)
      return true unless mode == 'e'
      return true if skip_confirmation

      count = application.files.length
      return true if count <= BULK_DELETE_THRESHOLD

      print "About to delete #{count} files (more than #{BULK_DELETE_THRESHOLD}). Type `y` to proceed: "
      answer = $stdin.gets
      return false if answer.nil?

      %w[y yes].include?(answer.strip.downcase)
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
        opt.on('--yes', 'Skip the bulk-delete confirmation in the execution mode') { @skip_confirmation = true }
        opt.on('--version', 'Print the version') { @action = :print_version }
        opt.on('-h', '--help', 'Print this help') { @action = :print_help }
      end
    end
  end
end
