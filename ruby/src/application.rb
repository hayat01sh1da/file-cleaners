require 'fileutils'

class Application
  class InvalidModeError < StandardError; end

  def self.run(dirname:, pattern:, mode: 'd')
    instance = new(dirname, pattern, mode)
    instance.validate_mode!
    instance.run
  end

  def initialize(dirname, pattern, mode)
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
    puts "Target dirname is #{Dir.getwd}"
    if !files.empty?
      puts "========== [#{exec_mode}] Total File Count to Clean: #{files.size} =========="
      puts "========== [#{exec_mode}] Start Cleaning #{pattern} =========="
      files.each { |file|
        puts "========== [#{exec_mode}] Cleaning #{file} =========="
      }
      FileUtils.rm_rf(files) if mode == 'e'
      puts "========== [#{exec_mode}] Cleaned #{pattern} =========="
      puts "========== [#{exec_mode}] Total Cleaned File Count: #{files.size} =========="
    else
      puts "========== [#{exec_mode}] No #{pattern} Remains =========="
    end
  end

  private

  attr_reader :pattern, :mode, :files

  def exec_mode
    mode == '-e' ? 'EXECUTION' : 'DRY RUN'
  end
end
