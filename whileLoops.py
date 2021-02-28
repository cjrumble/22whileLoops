# WHILE LOOP LESSON
# Whhile Loop

# Unlike the for loop which runs up to a certain no.of iterations, the while loop relies on a condition to complete the execution.

# While coding, there could be scenarios where you don’t know the cut - off point of a loop.
# For example, a program asking for user input indefinite number of times until he presses ESC key or reading a file until it finds a specific token.

# What is a While Loop?
# A while loop is a control flow structure which repeatedly executes a block of code indefinite no.of times until the given condition becomes false.For example, say, you want to count the occurrence of odd numbers in a range.Some technical references call it a pre-test loop as it checks the condition before every iteration.

# Python While Loop – Syntax
# while some condition ( or expression):
#     a block of code
# # The syntax is clearly stating that Python first evaluates the condition.

    If
    the
    check
    fails, then
    the
    control
    won’t
    enter
    into
    the
    loop
    instead
    will
    get
    transferred
    to
    the
    next
    statement.Whereas if the
    condition
    passes, then
    the
    statements
    inside
    the
    loop
    shall
    execute.

    This
    cycle
    would
    repeat
    itself
    until
    the
    while condition fails or returns false.When such a situation would occur, the loop would break and pass control to the next executable statement.

    1.2.Python
    While
    Loop
    Workflow

    Python
    while loop workflow

    1.3.While
    loop in Python – Example

    This
    example
    exhibits
    how
    to
    count
    the
    occurrences
    of
    odd
    numbers in a
    range
    entered
    by
    the
    user
    excluding
    the
    endpoints.


    # custom debug print function
    def dbgprint(x):
        if debug == True:
            print(x)


    # ask user to enter the range values
    debug = False
    r1 = int(input("Enter the starting range value?"))
    r2 = int(input("Enter the ending range value?"))

    dbgprint("Range: %d - %d" % (r1, r2))

    num = r1 + 1
    count = 0

    while num < r2:
        dbgprint("num: %d" % (num))
        res = num % 2
        dbgprint("res: %d" % (res))
        if (num % 2) > 0:
            count += 1
        num += 1

    print("Odd count: %d" % (count))
    Once
    you
    finish
    up
    the
    execution
    of
    the
    above
    code, you
    should
    see
    the
    following
    output.

    Enter
    the
    starting
    range
    value? 1
    Enter
    the
    ending
    range
    value? 100
    Odd
    count: 49
    In
    this
    program, we
    are
    using
    the
    following
    four
    variables.

    1.
    r1 – starting
    range
    value

    2.
    r2 – ending
    range
    value

    3.
    num – the
    variable
    we
    are
    testing
    for an odd number

    4.
    count – the
    counter
    variable, incremented
    upon
    every
    positive
    test

    We’ve
    initialized
    the “num” variable
    with the starting offset plus one and the counter variable with a zero.The loop is testing if “num” remains less than the ending offset value else it’ll break.

    In
    each
    iteration, the
    code
    block
    inside
    the
    loop is calculating
    the
    remainder
    of
    the “num” variable.A
    non - zero
    result
    would
    mean
    the
    number is odd and the “count” var
    would
    get
    incremented
    by
    one.

    The
    last
    statement in the
    while loop is stepping up the value of “num” by one, and it goes through for re-execution.The loop shall stop only after the value of the “num” is equal to or more than the ending range offset, i.e., “r2”.

    2.
    Else
    Clause
    with Python While Loop

    In
    Python, we
    can
    add
    an
    optional else clause
    after
    the
    end
    of “while ” loop.

    The
    code
    inside
    the else clause
    would
    always
    run
    but
    after
    the
    while loop finishes execution.The one situation when it won’t run is if the loop exits after a “break” statement.

    Using
    the else clause
    would
    make
    sense
    when
    you
    wish
    to
    execute
    a
    set
    of
    instructions
    after
    the
    while loop ends, i.e., without using a break statement.

    Let’s
    now
    see
    an
    example
    to
    demonstrate
    the
    use
    of “ else ” in the
    Python
    while loop.

    2.1.While
    Loop
    with Else in Python – Example


    def while_else_demo():

        count = 0
        while count < 5:
            num = int(input("Enter number between 0-100?"))
            if (num < 0) or (num > 100):
                print("Aborted while: You've entered an invalid number.")
                break
            count += 1
        else:
            print("While loop ended gracefully.")


    while_else_demo()
    The
    above
    program
    runs
    the
    while loop until the count is less than 5.

    It
    takes
    a
    number
    between
    0 - 100 as input.If
    you
    enter
    a
    valid
    number
    5
    times, then
    the
    while loop runs successfully, and the message from the else clause would get displayed.

    If
    you
    enter
    an
    invalid
    number, then
    the
    loop
    would
    get
    aborted
    without
    execting
    the
    code in the else.

    Iteration  # 1 While loop finishes with success and “else” clause executes.

    Enter
    number
    between
    0 - 100?1
    Enter
    number
    between
    0 - 100?2
    Enter
    number
    between
    0 - 100?3
    Enter
    number
    between
    0 - 100?4
    Enter
    number
    between
    0 - 100?5
    While
    loop
    ended
    gracefully.
    Iteration  # 2 While loop aborts and “else” clause won’t execute.

    Enter
    number
    between
    0 - 100?1
    Enter
    number
    between
    0 - 100?101
    Aborted
    while: You
    've entered an invalid number.
    While
    Loop in Python – Summary