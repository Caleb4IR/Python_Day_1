# Currying VS Partial

## Currying
- Currying is a process where a function takes a single argument and returns another function, which in turn takes a single argument, and so forth, until all arguments of the original function are accommodated. The output is a chain of functions.

### Example
#### Normal Function
```
def multiply(a, b, c):
  return a * b * c
  
```
#### Curried Function
```
def curried_multiply(a):
  def next(b):
      def final(c):
          return a * b * c
      return final
  return next
  
```

## Partial
- Partial application involves taking a function that accepts N arguments and supplying data for M arguments, where M is less than N. The result is a new function that accepts fewer arguments, specifically N - M arguments.

## Difference
- The key disparity lies in their approach to handling arguments. Currying solely transforms a function into a sequence of functions without binding any argument values, while partial application binds a subset of arguments to create a new function that accepts fewer arguments.