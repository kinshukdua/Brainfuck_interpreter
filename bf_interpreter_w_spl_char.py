import sys
import argparse
import string
import ast
import shlex

class InputError(SyntaxError):
    pass
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',type=str,help='Name of the source File')
    parser.add_argument('-c',type=int,default = 1,help='Does your file have comments? (0=>No, 1=>Yes)')
    args = parser.parse_args()
    filename = args.f
    with open(filename, "r") as f:  
        raw_code = f.read()
    if args.c:
        code = "".join([i for i in raw_code if i in '[],.<>+-'])
    else:
        code = raw_code.translate(str.maketrans('', '', string.whitespace))
    run(code,filename)
def run(code,filename):
    pntr= 0
    mem = [0]  
    def loop_init(pntr,index,loop_end):
        end = loop_end[index]
        while True:
            
            if mem[pntr] == 0:
                return pntr, end
            else:
                inner_index = index+1
                while inner_index < end:
                    inner_instruction = code[inner_index]
                    pntr,inner_index = execute[inner_instruction](pntr,inner_index,loop_end)
                    inner_index += 1
                
    def increment_pointer(pntr,index,*args):
        pntr += 1
        if len(mem)<=pntr+1:
            mem.append(0)
        return pntr, index
    def decrement_pointer(pntr,index,*args):
        pntr -= 1
        if pntr<0:
            raise MemoryError("starting of memory reached, pointer cannot decrement further")
        return pntr, index
    def increase_value(pntr,index,*args):
        mem[pntr] += 1
        return pntr, index
    def decrease_value(pntr,index,*args):
        mem[pntr] -= 1
        return pntr, index
    def input_(pntr,index,*args):
        inp=input("Input: ")
        if not inp.isdigit():
            inp=ast.literal_eval(shlex.quote(inp))
        
        if len(inp) > 1:
            raise InputError("Each cell can only hold 1 byte (1 character) of memory!")
        
        elif len(inp) == 0:
            raise InputError("Input cannot be empty")
        mem[pntr] = ord(inp)
        return pntr, index
    def output(pntr,index,*args):
        sys.stdout.write(str(chr(mem[pntr]%256)))
        sys.stdout.flush()
        #print(chr(mem[pntr]%256),)
        return pntr, index
    execute = {"[":loop_init, 
               "]":"",
               ">":increment_pointer,
               "<":decrement_pointer,
               "+":increase_value,
               "-":decrease_value,
               ".":output,
               ",":input_}
   
    def errorcheck(code):
        stack = []
        loop_end = {}
        for index,instruction in enumerate(code):
            if instruction == "[":
                stack.append(index)
            elif instruction == "]":
                try:
                    loop_end[stack.pop()]=index
                except:
                    raise SyntaxError('Extra close loop character "]"',(filename,1,index+1,code))
            elif instruction not in execute:
                raise SyntaxError(f'unknown instruction "{instruction}" found',(filename,1,index+1,code))
        if stack:
            raise SyntaxError('Extra open loop character "["',(filename,1,stack[-1]+1,code))
        else:
            return loop_end
    loop_end = errorcheck(code)
    index = 0
    while index < len(code):
        instruction = code[index]
        pntr,index = execute[instruction](pntr,index,loop_end)
        index += 1

if __name__ == '__main__':
    main()
                
            