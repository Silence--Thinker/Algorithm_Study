#!/usr/bin/env ruby
# -*- coding:utf-8 -*-

# 算法实现终稿
def reversal ()
    n = 100
    (1..n).each {|i|
        flag = false
        (1..n).each{|j|
            if i % j == 0       
                flag = !flag
            end
        }
        puts "#{i}" if flag
    }
end

def reversal_02 ()
    n = 100
    (1..n).each {|i|
        flag = false
        (2..n-1).each{|j|
            if i % j == 0       
                flag = !flag
            end
        }
        puts "#{i}" if flag==false
    }
end

# 算法实现 01
def reversal_01 ()
    n = 100
    cards = Array.new(n, false)

    # 从2到n翻牌
    (2..n).each {|i|
        j = i - 1
        while j < cards.size do
            cards[j] = !cards[j]
            j += i
        end
    }
    n.times{|i|
        puts i + 1 if !cards[i]
    }
end

# 算法逐渐优化
# reversal_01()
# reversal_02()
reversal()

