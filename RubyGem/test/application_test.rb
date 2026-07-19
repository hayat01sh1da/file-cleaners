# frozen_string_literal: true
# rbs_inline: enabled

require 'minitest/autorun'
require 'stringio'
require_relative '../lib/spreen_clean'

class ApplicationTest < Minitest::Test
  def setup
    @dirname = File.join('test', 'tmp')
    FileUtils.mkdir_p(dirname)
    1.upto(100).each { |i| File.write(File.join(dirname, "test_file_#{format('%03d', i)}.txt"), '') }
    @pattern = '*.txt'
    @io      = StringIO.new
  end

  def teardown
    FileUtils.rm_rf(dirname)
  end

  def test_invalid_mode
    error = assert_raises SpreenClean::Application::InvalidModeError do
      SpreenClean::Application.run(dirname:, pattern:, mode: 'a', io:)
    end
    assert_equal('a is invalid mode. Provide either `d`(default) or `e`.', error.message)
  end

  def test_run_in_dry_run_mode_with_default_mode
    SpreenClean::Application.run(dirname:, pattern:, io:)

    assert_equal(100, Dir.glob(File.join(dirname, '**', pattern)).length)
  end

  def test_run_in_dry_run_mode_with_explicit_d_mode
    SpreenClean::Application.run(dirname:, pattern:, mode: 'd', io:)

    assert_equal(100, Dir.glob(File.join(dirname, '**', pattern)).length)
  end

  def test_run_in_exec_mode
    SpreenClean::Application.run(dirname:, pattern:, mode: 'e', io:)

    assert_equal(0, Dir.glob(File.join(dirname, '**', pattern)).length)
  end

  def test_run_announces_the_dry_run_progress
    SpreenClean::Application.run(dirname:, pattern:, io:)

    assert_includes(io.string, "Target dirname is #{File.absolute_path(dirname)}")
    assert_includes(io.string, '========== [DRY RUN] Total File Count to Clean: 100 ==========')
    assert_includes(io.string, "========== [DRY RUN] Cleaning #{File.join(dirname, 'test_file_001.txt')} ==========")
  end

  def test_run_announces_the_execution_progress
    SpreenClean::Application.run(dirname:, pattern:, mode: 'e', io:)

    assert_includes(io.string, '========== [EXECUTION] Start Cleaning *.txt ==========')
    assert_includes(io.string, '========== [EXECUTION] Cleaned *.txt ==========')
    assert_includes(io.string, '========== [EXECUTION] Total Cleaned File Count: 100 ==========')
  end

  def test_run_announces_empty_when_nothing_matches
    SpreenClean::Application.run(dirname:, pattern: '*.log', io:)

    assert_includes(io.string, '========== [DRY RUN] No *.log Remains ==========')
  end

  def test_run_refuses_a_filesystem_root
    error = assert_raises SpreenClean::Application::RootDirnameError do
      SpreenClean::Application.run(dirname: '/', pattern:, io:)
    end
    assert_equal('/ is a filesystem root. Provide a narrower dirname.', error.message)
    assert_empty(io.string)
  end

  private

  attr_reader :dirname, :pattern, :io
end
