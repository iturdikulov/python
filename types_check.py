from typing import Callable, reveal_type
from collections.abc import Iterable, Iterator

#  ___       _
# |_ _|_ __ | |_ _ __ ___
#  | || '_ \| __| '__/ _ \
#  | || | | | |_| | | (_) |
# |___|_| |_|\__|_|  \___/

# Type inference
# mypy will infer the correct type based on what is initially assigned to the
# variable.
i = 1
reveal_type(i)

my_list = [1, 2]
reveal_type(my_list)


# The "name: str" annotation says that the "name" argument should be a string
# The "-> str" annotation says that "greeting" will return a string
def greeting(name: str) -> str:
    return "Hello " + name


# No error
greeting("World!")

greeting(3)

greeting(b"Alice")


# Unsupported operand types for * ("str" and "str")
def bad_greeting(name: str) -> str:
    return "Hello " * name  # type: ignore


# list[str] is a subtype of Iterable[str]
def greet_all(names: Iterable[str]) -> None:
    for name in names:
        print("Hello " + name)


names = ["Alice", "Bob", "Charlie"]
ages = [10, 20, 30]

greet_all(names)  # Ok!
greet_all(ages)  # Error due to incompatible types


def normalize_id(user_id: int | str) -> str:
    # mypy understands basic isinstance checks and so can infer that the
    # user_id variable was of type int in the if-branch and of type str in the
    # else-branch.
    if isinstance(user_id, int):
        return f"user-{100_000 + user_id}"
    else:
        return user_id


def nums_below(numbers: Iterable[float], limit: float) -> list[float]:
    output: list[float] = []
    for num in numbers:
        if num < limit:
            output.append(num)
    return output


#   ____ _                _     ____  _               _
#  / ___| |__   ___  __ _| |_  / ___|| |__   ___  ___| |_
# | |   | '_ \ / _ \/ _` | __| \___ \| '_ \ / _ \/ _ \ __|
# | |___| | | |  __/ (_| | |_   ___) | | | |  __/  __/ |_
#  \____|_| |_|\___|\__,_|\__| |____/|_| |_|\___|\___|\__|

# Variables (almost redundant)

age: int = 1
a: int
a = "1"  # incompatible types

child: bool
if age < 18:
    child = 1  # incompatible types
else:
    child = False

# Built-in types

# Note that mypy can usually infer the type of a variable from its value,
# so technically these annotations are redundant
x1: int = 1
x2: float = 1.0
x3: bool = True
x4: str = "Hello"
x5: bytes = b"World"

# Collections
x6: list[int] = [1]
x7: set[int] = {1, 2, 3}

# Mappings
x8: dict[str, float] = {"field": 2.0}
x9: tuple[int, str, float] = (41, "42", 43)  # fixed size tuple

# Unions and Optionals
x10: list[int | str] = [3, 5, "test", "fun", True]
x11: int | None = None


# Functions
def untyped(x):
    x.anything() + 1 + "string"  # no errors


def stringify(num: int) -> str:
    return str(num)
_ = stringify(10)


def plus(num1: int, num2: int) -> int:
    return num1 + num2
_ = plus(10, 20)


def show(value: str, excitement: int = 10) -> None:
    print(value + "!" * excitement)
_ = show("Hello")

x: Callable[[str, int], float] = f
def register(callback: Callable[[str], int]) -> None: ...


def gen(n: int) -> Iterator[int]:
    i = 0
    while i < n:
        yield i
        i += 1


def send_email(
    address: str | list[str],
    sender: str,
    cc: list[str] | None = None,
    bcc: list[str] | None = None,
    subject: str = "",
    body: list[str] | None = None,
) -> None:
    print(sender, cc, bcc, subject, body)


# def quux1(positional_or_keyword_parameters, *, keyword_only_parameters):
#     pass
# def quux2(positional_only_parameters, /, positional_or_keyword_parameters,
#          *, keyword_only_parameters):
def quux(x: int, /, *, y: int) -> None:
    pass

quux(3, y=5)    # Ok
quux(3, 5)      # error: Too many positional arguments for "quux"
quux(x=3, y=5)  # error: Unexpected keyword argument "x" for "quux"

def call(self, *args: str, **kwargs: str) -> str:
    reveal_type(args)  # Revealed type is "tuple[str, ...]"
    reveal_type(kwargs)  # Revealed type is "dict[str, str]"
    request = make_request(*args, **kwargs)
    return self.do_api_query(request)

# Classes

from typing import ClassVar

class BankAccount:
    # The "__init__" method doesn't return anything, so it gets return
    # type "None" just like any other method that doesn't return anything
    def __init__(self, account_name: str, initial_balance: int = 0) -> None:
        # mypy will infer the correct types for these instance variables
        # based on the types of the parameters.
        self.account_name = account_name
        self.balance = initial_balance

    # For instance methods, omit type for "self"
    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        self.balance -= amount

# User-defined classes are valid as types in annotations
account: BankAccount = BankAccount("Alice", 400)
def transfer(src: BankAccount, dst: BankAccount, amount: int) -> None:
    src.withdraw(amount)
    dst.deposit(amount)

# Functions that accept BankAccount also accept any subclass of BankAccount!
class AuditedBankAccount(BankAccount):
    # You can optionally declare instance variables in the class body
    audit_log: list[str]

    def __init__(self, account_name: str, initial_balance: int = 0) -> None:
        super().__init__(account_name, initial_balance)
        self.audit_log: list[str] = []

    def deposit(self, amount: int) -> None:
        self.audit_log.append(f"Deposited {amount}")
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        self.audit_log.append(f"Withdrew {amount}")
        self.balance -= amount

audited = AuditedBankAccount("Bob", 300)
transfer(audited, account, 100)  # type checks!
