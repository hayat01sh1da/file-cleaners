require 'fileutils'

class Application
  class InvalidModeError < StandardError; end

  def self.run(dirname: '.', pattern: '*', mode: 'd')
    instance = new(dirname:, pattern:, mode:)
    instance.validate_mode!
    instance.run
  end

  def initialize(dirname: '.', pattern: '*', mode: 'd')
    @dirname = dirname
    @pattern = pattern
    @mode    = mode
    @files   = Dir.glob(File.join(dirname, '**', pattern))
  end

  def validate_mode!
    case mode
    when 'd', 'e'
      return
    else
      raise InvalidModeError, "#{mode} is invalid mode. Provide either `d`(default) or `e`."
    end
  end

  def run
    output "Target dirname is #{File.absolute_path(dirname)}"
    output "========== [#{exec_mode}] No #{pattern} Remains ==========" and return if files.empty?
    output "========== [#{exec_mode}] Total File Count to Clean: #{files.size} =========="
    output "========== [#{exec_mode}] Start Cleaning #{pattern} =========="
    files.each { |file|
      output "========== [#{exec_mode}] Cleaning #{file} =========="
    }
    FileUtils.rm_rf(files) if mode == 'e'
    output "========== [#{exec_mode}] Cleaned #{pattern} =========="
    output "========== [#{exec_mode}] Total Cleaned File Count: #{files.size} =========="
  end

  private

  attr_reader :dirname, :pattern, :mode, :files

  def exec_mode
    mode == 'e' ? 'EXECUTION' : 'DRY RUN'
  end

  def test_env?
    caller[-1].split('/').last.match?(/minitest\.rb/)
  end

  def output(message)
    puts message unless test_env?
  end
end
