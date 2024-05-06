require 'fileutils'

class Application
  def self.run(dirname:, filename:, mode: nil)
    self.new(dirname, filename, mode).run
  end

  def initialize(dirname, filename, mode)
    @filename = filename
    @mode     = mode
    @files    = Dir.glob(File.join(dirname, '**', filename))
  end

  def run
    puts "Target dirname is #{Dir.getwd}"
    if !files.empty?
      puts "========== [#{exec_mode}] Total File Count to Clean: #{files.size} =========="
      puts "========== [#{exec_mode}] Start Cleaning #{filename} =========="
      files.each { |file|
        puts "========== [#{exec_mode}] Cleaning #{file} =========="
      }
      FileUtils.rm_rf(files) if mode == '-e'
      puts "========== [#{exec_mode}] Cleaned #{filename} =========="
      puts "========== [#{exec_mode}] Total Cleaned File Count: #{files.size} =========="
    else
      puts "========== [#{exec_mode}] No #{filename} Remains =========="
    end
  end

  private

  attr_reader :filename, :mode, :files

  def exec_mode
    mode == '-e' ? 'EXECUTION' : 'DRY RUN'
  end
end
