import os
import subprocess
import sys

prog = r'''
main(){unsigned char *x=calloc(12,1);unsigned char *l=x;++*x; ++*x; ++*x; ++*x; ++*x; ++*x; ++*x; ++*x;++*x; ++*x;while(*x){++x;++*x; ++*x; ++*x; ++*x;++*x; ++*x;++*x;++x;
   ++*x; ++*x; ++*x; ++*x; ++*x; ++*x; ++*x; ++*x;++*x; ++*x;++x;++*x; ++*x;++*x;++x;++*x; ++*x; ++*x; ++*x; ++*x; ++*x; ++*x; ++*x;++*x;--x; --x; --x; --x;--*x;}++x;++*x; ++*x;
     putchar(*x);++x;++*x;putchar(*x);++*x; ++*x; ++*x; ++*x;++*x; ++*x;++*x;putchar(*x); putchar(*x);++*x; ++*x;++*x;putchar(*x);++x;++*x; ++*x;putchar(*x);++x;
   --*x; --*x;--*x;putchar(*x);--x; --x;putchar(*x);++*x; ++*x;++*x;putchar(*x);--*x; --*x; --*x; --*x;--*x; --*x;putchar(*x);--*x; --*x; --*x; --*x; --*x; --*x; --*x; --*x;putchar(*x);
  ++x;++*x;putchar(*x);free(l);}
'''

if not os.path.exists('foo'):
    f = open('foo.c', 'w')
    f.write(prog)
    f.close()
    subprocess.call(["gcc", "foo.c", "-ofoo", "-std=c99", '-w', '-Ofast'])
subprocess.call(["./foo"], stdin=sys.stdin)
