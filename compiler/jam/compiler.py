import logging
from io import IOBase
from subprocess import check_output

from . import parser
from ..lekvar import lekvar
from ..llvm import emitter as llvm
from ..llvm.builtins import builtins
from ..errors import CompilerError

def compileRun(path:str, target:str, logger = logging.getLogger()):
    compileFile(path, target, logger)
    return check_output(["lli", target])

def compileFile(path:str, target:str, logger = logging.getLogger()):
    with open(path, "r") as input, open(target, "w") as output:
        compile(input, output)

def compile(input:IOBase, output:IOBase, logger = logging.getLogger()):
    try:
        # Produce lekvar
        ir = parser.parseFile(input)
        lekvar.verify(ir, builtins(), logger)
        # Emit LLVM
        output.write(llvm.emit(ir, logger).decode("UTF-8"))
    except CompilerError as err:
        # Format the error and re-raise
        input.seek(0)
        err.format(input.read())
        raise err

