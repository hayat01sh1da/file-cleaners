# frozen_string_literal: true
# rbs_inline: enabled

require 'minitest/autorun'
require 'stringio'
require_relative '../lib/spreen_clean'

class CLITest < Minitest::Test
  def setup
    @dirname = File.join('test', 'tmp')
    FileUtils.mkdir_p(dirname)
    1.upto(10).each { |i| File.write(File.join(dirname, "test_file_#{format('%03d', i)}.txt"), '') }
    @pattern = '*.txt'
  end

  def teardown
    FileUtils.rm_rf(dirname)
  end

  def test_dry_run_by_default
    status = nil
    out, _err = capture_io { status = SpreenClean::CLI.start([pattern, '--dirname', dirname]) }

    assert_equal(0, status)
    assert_includes(out, '========== [DRY RUN] Total File Count to Clean: 10 ==========')
    assert_equal(10, Dir.glob(File.join(dirname, '**', pattern)).length)
  end

  def test_execution_mode
    status = nil
    out, _err = capture_io { status = SpreenClean::CLI.start([pattern, '--dirname', dirname, '--mode', 'e']) }

    assert_equal(0, status)
    assert_includes(out, '========== [EXECUTION] Total Cleaned File Count: 10 ==========')
    assert_equal(0, Dir.glob(File.join(dirname, '**', pattern)).length)
  end

  def test_default_pattern_matches_everything
    status = nil
    out, _err = capture_io { status = SpreenClean::CLI.start(['--dirname', dirname]) }

    assert_equal(0, status)
    assert_includes(out, '========== [DRY RUN] Total File Count to Clean: 10 ==========')
    assert_equal(10, Dir.glob(File.join(dirname, '**', pattern)).length)
  end

  def test_invalid_mode
    status = nil
    _out, err = capture_io { status = SpreenClean::CLI.start([pattern, '--dirname', dirname, '--mode', 'a']) }

    assert_equal(1, status)
    assert_match(/invalid argument/, err)
    assert_equal(10, Dir.glob(File.join(dirname, '**', pattern)).length)
  end

  def test_root_dirname_refused
    status = nil
    _out, err = capture_io { status = SpreenClean::CLI.start([pattern, '--dirname', '/', '--mode', 'e']) }

    assert_equal(1, status)
    assert_match(/is a filesystem root/, err)
  end

  def test_bulk_execution_aborts_when_declined
    make_bulk_files
    status = nil
    out, _err = with_stdin("n\n") do
      capture_io { status = SpreenClean::CLI.start([pattern, '--dirname', dirname, '--mode', 'e']) }
    end

    assert_equal(1, status)
    assert_includes(out, 'About to delete 101 files (more than 100). Type `y` to proceed: ')
    assert_equal(101, Dir.glob(File.join(dirname, '**', pattern)).length)
  end

  def test_bulk_execution_proceeds_when_confirmed
    make_bulk_files
    status = nil
    with_stdin("y\n") do
      capture_io { status = SpreenClean::CLI.start([pattern, '--dirname', dirname, '--mode', 'e']) }
    end

    assert_equal(0, status)
    assert_equal(0, Dir.glob(File.join(dirname, '**', pattern)).length)
  end

  def test_bulk_execution_skips_confirmation_with_yes_flag
    make_bulk_files
    status = nil
    out, _err = capture_io { status = SpreenClean::CLI.start([pattern, '--dirname', dirname, '--mode', 'e', '--yes']) }

    assert_equal(0, status)
    refute_includes(out, 'About to delete')
    assert_equal(0, Dir.glob(File.join(dirname, '**', pattern)).length)
  end

  def test_version
    status = nil
    out, _err = capture_io { status = SpreenClean::CLI.start(['--version']) }

    assert_equal(0, status)
    assert_equal("#{SpreenClean::VERSION}\n", out)
  end

  def test_help
    status = nil
    out, _err = capture_io { status = SpreenClean::CLI.start(['--help']) }

    assert_equal(0, status)
    assert_match(/Usage: file-clean \[PATTERN\] \[options\]/, out)
  end

  private

  attr_reader :dirname, :pattern

  # Tops the fixture up beyond BULK_DELETE_THRESHOLD (101 files in total).
  def make_bulk_files
    11.upto(101).each { |i| File.write(File.join(dirname, "test_file_#{format('%03d', i)}.txt"), '') }
  end

  # @rbs input: String
  # @rbs &block: () -> [String, String]
  # @rbs return: [String, String]
  def with_stdin(input, &)
    original = $stdin
    $stdin   = StringIO.new(input)
    yield
  ensure
    $stdin = original
  end
end
