# def play_pass(str, n)
#     #your code
#     result = ""
#     str.each_chr_with_index do |id, chr|
#         if chr.isalpha?
#             chr_idx = chr.ord - "A".ord
#             new_chr_idx = (chr_idx + n) % 26
#             new_chr = ("A".ord + new_chr_idx).chr
#             if id % 2 != 0
#                 new_chr = new_chr.downcase
#             result += new_chr
#         elsif chr.to_i?
#             result += (9 - chr.to_i).to_s
#         else
#             result += chr
#         end
#     end
#     return result.reverse
# end

def sum(arr)
    result = 0
    arr.each {|num| result += num}
    return result
end

def queue_time_2(customers, n)
    #your code here
    if customers.length == 1
        return customers[0]
    end
    if n == 1
        return sum(customers)
    end
    if n >= customers.length
        return customers.max
    end
    # num of tills < num of que
    customers_arr = customers
    # p customers_arr
    tills = []
    n.times {tills.push(customers_arr.shift)}
    # p tills
    counts = 0
    while true
        counts += 1
        tills.each.with_index do |num, idx|
            # p num, idx
            if tills[idx] >= 1
                tills[idx] = num - 1
            end
            if tills[idx] == 0
                if customers_arr.length != 0
                    tills[idx] = customers_arr.shift
                end
            end
        end

        if customers_arr.length == 0
            p customers_arr, tills, counts
            return tills.max + counts
        end

    end
    return counts
end

def queue_time(customers, lines)
    tills = Array.new(lines, 0)

    customers.each do |c|
        min = tills.min
        i = tills.index{|val| val == min }
        tills[i] += c
        p tills
    end

    tills.max
  end

# p queue_time([2,2,3,3,4,4], 2)
# p queue_time([1,2,3,4,5], 100)
p queue_time([0, 870, 49, 98, 28, 50, 24, 955], 6)
# choose smallest que and add that













