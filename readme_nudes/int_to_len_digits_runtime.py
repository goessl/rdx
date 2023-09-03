import timeit
import matplotlib.pyplot as plt



N = 1000
ls, ts = list(range(1, 3000, 10)), []
for l in ls:
    s = l*'3'
    ts += [timeit.timeit('int_to_len_digits('+s+')',
                setup='from rdx import int_to_len_digits', number=N) /
            timeit.timeit('len(int_to_digits('+s+'))',
                    setup='from rdx import int_to_digits', number=N)]
plt.plot(ls, ts, color='C0', label='int_to_len_digits(n)')
plt.axhline(1, color='C1', label='len(int_to_digits(n))')

plt.title('Relative execution time')
plt.xlabel('x')
plt.xticks((1, 1000, 2000, 3000), ('3', "1000*'3'", "2000*'3'", "3000*'3'"))
plt.ylabel('t')
plt.yscale('log')
plt.legend()
#plt.show()
plt.savefig('int_to_len_digits_runtime.png', dpi=300)
