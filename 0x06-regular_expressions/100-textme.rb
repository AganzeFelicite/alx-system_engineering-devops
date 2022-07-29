#!/usr/bin/env ruby
#dealing with a message log file
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(",")

