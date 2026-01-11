A wrapper function is created, and an original function is also created.
The original function is passed into the wrapper function.
Inside the wrapper, another function (before) is defined which executes its own code and then executes the original function’s code.
The wrapper returns this inner function, sothe whole wrapper stored in a variable when that is called it gives both the original code and extra behavior.
