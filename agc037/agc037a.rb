s = gets.strip
t = ""
k = 0
prev = ""
(0..s.length - 1).each do |i|
  t += s[i]
  if prev != t
    k += 1
    prev = t
    t = ""
  end
end
puts k
