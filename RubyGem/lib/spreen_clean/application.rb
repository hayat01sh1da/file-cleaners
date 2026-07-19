# frozen_string_literal: true
# rbs_inline: enabled

require 'fileutils'

module SpreenClean
  # Deletes files in a directory tree matching a glob pattern, with a dry-run
  # mode that prints what would be removed without touching the filesystem.
  class Application
    class InvalidModeError < StandardError; end

    # @rbs dirname: String
    # @rbs pattern: String
    # @rbs mode: String
    # @rbs io: IO
    # @rbs return: void
    def self.run(dirname: '.', pattern: '*', mode: 'd', io: $stdout)
      instance = new(dirname:, pattern:, mode:, io:)
      instance.validate_mode!
      instance.run
    end

    # @rbs dirname: String
    # @rbs pattern: String
    # @rbs mode: String
    # @rbs io: IO
    # @rbs return: void
    def initialize(dirname: '.', pattern: '*', mode: 'd', io: $stdout)
      @dirname = dirname
      @pattern = pattern
      @mode    = mode
      @io      = io
      @files   = Dir.glob(File.join(dirname, '**', pattern))
    end

    # @rbs return: void
    def validate_mode!
      case mode
      when 'd', 'e'
        nil
      else
        raise InvalidModeError, "#{mode} is invalid mode. Provide either `d`(default) or `e`."
      end
    end

    # @rbs return: void
    def run
      output "Target dirname is #{File.absolute_path(dirname)}"
      return announce_empty if files.empty?

      announce_start
      clean_files
      announce_finish
    end

    private

    attr_reader :dirname #: String
    attr_reader :pattern #: String
    attr_reader :mode #: String
    attr_reader :io #: IO
    attr_reader :files #: Array[String]

    # @rbs return: void
    def announce_empty
      output "========== [#{exec_mode}] No #{pattern} Remains =========="
    end

    # @rbs return: void
    def announce_start
      output "========== [#{exec_mode}] Total File Count to Clean: #{files.length} =========="
      output "========== [#{exec_mode}] Start Cleaning #{pattern} =========="
    end

    # @rbs return: void
    def clean_files
      files.each { |file| output "========== [#{exec_mode}] Cleaning #{file} ==========" }
      FileUtils.rm_rf(files) if mode == 'e'
    end

    # @rbs return: void
    def announce_finish
      output "========== [#{exec_mode}] Cleaned #{pattern} =========="
      output "========== [#{exec_mode}] Total Cleaned File Count: #{files.length} =========="
    end

    # @rbs return: String
    def exec_mode
      @exec_mode ||= mode == 'e' ? 'EXECUTION' : 'DRY RUN'
    end

    # @rbs message: String
    # @rbs return: void
    def output(message)
      io.puts message
    end
  end
end
