'''
difference between an iterator and an iterable?

iterable --> an object that has __iter__ method defined.
iterator --> an object that has both __iter__ and __next__ method defined where iter will return the iterator object and next will return
the next object in the iteration.



#generator vs iterator, which one to use and when?
generator is great for memory efficient data processing.
whenever we call the yield, the function stops and saves its state, it yields the value out.
'''