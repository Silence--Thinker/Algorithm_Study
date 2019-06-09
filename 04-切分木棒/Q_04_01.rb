#!/usr/bin/env ruby
# -*- coding:utf-8 -*-

def cuttingStick(n, m, current)

    if current >= n
        return 0
    elsif current < m 
        return 1 + cuttingStick(n, m, current * 2)
    else
        return 1 + cuttingStick(n, m, current + m)
    end
end

puts cuttingStick(20, 3, 1)
puts cuttingStick(100, 5, 1) 