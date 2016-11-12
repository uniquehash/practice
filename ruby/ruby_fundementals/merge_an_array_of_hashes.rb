
# look here for more background and other solutions source A
# http://stackoverflow.com/questions/17409744/how-do-i-merge-two-arrays-of-hashes-based-on-same-hash-key-value

# the docs for enumerable#flat_map  http://ruby-doc.org/core-2.0.0/Enumerable.html#flat_map-instance_method
# the docs for hash#update 			http://ruby-doc.org/core-2.0.0/Hash.html#update-instance_method


aa = [{"b"=>100,"a"=>101, "f"=>30}, {"a"=>102,"b"=>103, "f"=>25}, {"a"=>104,"b"=>105, "f"=> 40}]    
bb = [{"a"=>106,"b"=>107, "e"=>425, "f"=> 30}, {"a"=>108,"b"=>109, "e"=>55, "f"=>25}, {"a"=>138,"b"=>139, "e"=>67, "f"=>89}]

# p "step 1"
# p aa.zip(bb).flat_map{|k,v| next  k.update(v) if v != nil }
# p aa.zip(bb).flat_map{|k,v| 	
# 	if v != nil && v.fetch("f") == k.fetch("f")
# 		k['checked'] = true
# 		k		
# 	else
# 		k['checked'] = false
# 		k
# 	end
# }

p "step 2"
z = aa - bb
p z


# p "step 2"
# p aa.zip(bb).each 


