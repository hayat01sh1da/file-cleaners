require 'fileutils'

class Application
  def self.run(dirname:, pattern:, mode: nil)
    self.new(dirname, pattern, mode).run
  end

  def initialize(dirname, pattern, mode)
    @pattern = pattern
    @mode    = mode
    @files   = Dir.glob(File.join(dirname, '**', pattern))
  end

  def run
    puts "Target dirname is #{Dir.getwd}"
    if !files.empty?
      puts "========== [#{exec_mode}] Total File Count to Clean: #{files.size} =========="
      puts "========== [#{exec_mode}] Start Cleaning #{pattern} =========="
      files.each { |file|
        puts "========== [#{exec_mode}] Cleaning #{file} =========="
      }
      FileUtils.rm_rf(files) if mode == '-e'
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
