#!/usr/bin/env ruby
# -*- coding:utf-8 -*-

def cuttingStick(n, m)
    count = 0
    current = 1
    while n > current
        if current > m
            current += m
            count += 1
        else
            current *= 2
            count += 1
        end
    end
    return count
end

puts cuttingStick(20, 3)
puts cuttingStick(100, 5)