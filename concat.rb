def play_pass(str, n)
    #your code
    result = ""
    str.each_chr_with_index do |id, chr|
        if chr.isalpha?
            chr_idx = chr.ord - "A".ord
            new_chr_idx = (chr_idx + n) % 26
            new_chr = ("A".ord + new_chr_idx).chr
            if id % 2 != 0
                new_chr = new_chr.downcase
            result += new_chr
        elsif chr.to_i?
            result += (9 - chr.to_i).to_s
        else
            result += chr
        end
    end
    return result.reverse
end