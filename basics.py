# Vars start with letter or underscore and then consist of only nums, letters, underscores
# They're case-sensitive... you know that right?
# snake_case is the naming convention, stop using camelCase :(
# vars like __var__ are private and should be left alone
# None = nothing ~ like null
# Double vs Single quotes = they actually don't matter which, I thought they did :(
# You'd just need to do like this "To say 'really...'" or this "to say 'really really.'"
# Escape chars ~ \n, \"
# multiplying *= 5
# f strings -  looks like f"this is the {x} time that's happened"
# vars have truthiness and falsiness - 1 is true 0, empty, None = false
# comparisons == != > < >= <=
# and or not
# == = is the value/s the same while is = is the memory location the same
# range ~ typically used for for loops
# range(7) - 0 through 6
# range(1,8) - 1 through 7
# range(1, 10, 2) odds 1 to 10
# range(7, 0, -1) decrement
# break out of loops with: break
# list = [] ~ len(list) - OR ~ list(range(1,4))
# to decrement in lists its just list[-1] etc
# Remember the in method
#------------List Basics-----------------------
# Items in lists are mutable
# .append() - one item at the end to append (if you passed a list it would be a nested value
# .insert(<insertionPosition>, <val>) -
# .extend() - used for multiple items or to add another list
# .clear() - removes everything
# .pop(<index> or nothing) - removes last item by default or item at index specified
# .remove(<value>) - removes first occurrence of that value, throws error if not found
# .index(<value>) - returns index of the passed value
# .count(<value>) - nmumber of times value appears in list
# .reverse()
# .sort() - ascending order in place
# .join() - use as "<value>".join(<list>) to join together seperated by passed value
# Slices!
# list[start:end:step] - : need to be included or else it'll just return val at that index
# ex: list[1:] - index 1 to end OR list[-3:] returns last three values
# can make a copy in dif mem space with list2 = list[:]
# ex: list[2:4] or list[:3]
# finally count by 2 across a range ~ list[:10:2]
# reverse a list ~ list_r = list[::-1]
# can swap in lists by doing names[0], names[1] = names[1], names[0]
# --------------List Comprehension-----------------------
# new_list_from_old = [num * 2 for num in numbers]
# [<your_operation> for <item_to_operate_on> in <list>]
# You can use conditional logic in there too!
# list2 = [num for num in numbers if num is True]
