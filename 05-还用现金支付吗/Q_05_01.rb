#!/usr/bin/env ruby
# -*- coding: utf-8 -*-

coins = [10, 50, 100, 500]
cnt = 0

puts "====#{coins.shift}"

(2..15).each do |i|
    coins.repeated_combination(i).each do |coin_set|
        cnt += 1 if coin_set.inject(:+) == 1000
    end
end

puts cnt
