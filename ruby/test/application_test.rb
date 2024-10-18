require 'minitest/autorun'
require_relative '../src/application'

class ApplicationTest < Minitest::Test
  def setup
    @dirname = File.join('test', 'tmp')
    Dir.mkdir(dirname) unless Dir.exist?(dirname)
    1.upto(100).each { |i| IO.write(File.join(dirname, "test_file_#{format('%03d', i)}.txt"), '') }
    @pattern = '*.txt'
  end

  def teardown
    FileUtils.rm_rf(dirname)
  end

  def test_run_in_dry_run_mode_1
    Application.run(dirname:, pattern:)
    assert_equal(Dir.glob(File.join(dirname, '**', pattern)).size, 100)
  end

  def test_run_in_dry_run_mode_2
    Application.run(dirname:, pattern:, mode: '-d')
    assert_equal(Dir.glob(File.join(dirname, '**', pattern)).size, 100)
  end

  def test_run_in_exec_mode
    Application.run(dirname:, pattern:, mode: '-e')
    assert_equal(Dir.glob(File.join(dirname, '**', pattern)).size, 0)
  end

  private

  attr_reader :dirname, :pattern
end
