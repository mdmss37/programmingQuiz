# There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

# The function has two input variables:

# customers: an array (list in python) of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
# n: a positive integer, the number of checkout tills.
# The function should return an integer, the total time required.

# Assume that the front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free. So, for example:

# queue_time([5,3,4], 1)
# # should return 12
# # because when n=1, the total time is just the sum of the times

# queue_time([10,2,3,3], 2)
# # should return 10
# # because here n=2 and the 2nd, 3rd, and 4th people in the
# # queue finish before the 1st person has finished.

# queue_time([2,3,10], 2)
# # should return 12
# N.B. You should assume that all the test input will be valid, as specified above.

# P.S. The situation in this kata can be likened to the more-computer-science-related idea of a thread pool, with relation to running multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool

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

# solution from jrmarks11
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













