# frozen_string_literal: true
# rbs_inline: enabled

# Deletes files in a directory tree matching a glob pattern, with a dry-run
# mode that prints what would be removed without touching the filesystem.
class Application
  class InvalidModeError < StandardError; end

  # @rbs dirname: String
  # @rbs pattern: String
  # @rbs mode: String
  # @rbs return: void
  def self.run(dirname: '.', pattern: '*', mode: 'd')
    instance = new(dirname:, pattern:, mode:)
    instance.validate_mode!
    instance.run
  end

  # @rbs dirname: String
  # @rbs pattern: String
  # @rbs mode: String
  # @rbs return: void
  def initialize(dirname: '.', pattern: '*', mode: 'd')
    @dirname = dirname
    @pattern = pattern
    @mode    = mode
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

  attr_reader :dirname, :pattern, :mode, :files

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

  # @rbs return: bool
  def test_env?
    caller(0..0).first.split('/').last.include?('minitest.rb')
  end

  # @rbs message: String
  # @rbs return: void
  def output(message)
    puts message unless test_env?
  end
end
