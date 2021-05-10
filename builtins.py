print(any([0,0,0,0]))

widget_one = ''
widget_two = ''
widget_three = ''
widgets_exist = any([widget_one, widget_two, widget_three])
print (widgets_exist)

#exec: it executes the dynamically created program, which is either a string or a code object.
program= 'a = 5\nb=10\nprint("Sum =", a+b)'
print(exec(program))