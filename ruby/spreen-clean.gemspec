# frozen_string_literal: true

require_relative 'lib/spreen_clean/version'

Gem::Specification.new do |spec|
  spec.name    = 'spreen-clean'
  spec.version = SpreenClean::VERSION
  spec.authors = ['hayat01sh1da']

  spec.summary     = 'Spreen your workspace: delete files matching a glob pattern, dry run first.'
  spec.description = "Spreen — the falcon's stoop, then the preen. Deletes files in a directory tree " \
                     'matching a glob pattern via the file-clean CLI, defaulting to a dry-run mode that ' \
                     'prints every file that would be removed; pass `--mode e` to actually delete them.'
  spec.homepage = 'https://github.com/hayat01sh1da/spreen-clean'
  spec.license  = 'MIT'
  spec.required_ruby_version = '>= 3.4'

  spec.metadata['homepage_uri']          = spec.homepage
  spec.metadata['source_code_uri']       = spec.homepage
  spec.metadata['changelog_uri']         = "#{spec.homepage}/blob/master/CHANGELOG.md"
  spec.metadata['bug_tracker_uri']       = "#{spec.homepage}/issues"
  spec.metadata['rubygems_mfa_required'] = 'true'

  spec.files         = Dir['exe/*', 'lib/**/*.rb', 'sig/**/*.rbs', 'README.md', 'LICENSE.txt']
  spec.bindir        = 'exe'
  spec.executables   = ['file-clean']
  spec.require_paths = ['lib']
end
