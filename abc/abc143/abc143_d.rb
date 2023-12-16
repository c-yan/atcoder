N = gets.to_i
L = gets.strip.split.map(&:to_i)

L.sort!
result = 0
(0..N - 3).each do |i|
  (i + 1..N - 2).each do |j|
    t = L[i] + L[j]
    idx = L.bsearch_index { |x| x >= t }
    result += (idx ? idx : L.size) - j - 1
  end
end
puts result
