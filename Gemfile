source "https://rubygems.org"

gem "jekyll-theme-chirpy", "~> 4.0", ">= 4.0.0"

group :jekyll_plugins do
  # If you have any plugins, put them here!
  # gem "jekyll-xxx", "~> x.y"
  gem "jekyll-feed"
  gem "jekyll-paginate"
  gem "jekyll-redirect-from"
  gem "jekyll-seo-tag"
  gem "jekyll-archives"
  gem "jekyll-sitemap"
  gem "jekyll-target-blank"
  gem "jemoji"
  gem "jekyll-minifier"
  gem "jekyll-analytics"
  gem "jekyll-liquify"
end

group :test do
  gem "html-proofer", "~> 3.18"
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :install_if => Gem.win_platform?
