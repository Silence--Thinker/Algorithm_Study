#!/usr/bin/env ruby
# -*- coding:utf-8 -*-

# 问题: 求用十进制、二进制、八进制表示都是回文数的所有数字中，大于十进制数10的最小最

def palindromicNum ()
    num = 11
    while true
        if num.to_s == num.to_s.reverse &&
        num.to_s(2) == num.to_s(2).reverse &&
        num.to_s(8) == num.to_s(8).reverse 
        puts '结果是: '
        puts "十进制: #{num}"
        puts '二进制: ' + num.to_s(2)
        puts '八进制: ' + num.to_s(8)
        break
        else
            num += 2
        end
    end
end

palindromicNum()