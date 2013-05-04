/* 
 * From 3-15 "Algorithm Design Manual"
 * 
 * - Design a data structure that allows O(1) search, insert, and delete of integers.
 * - m + n units of space available, where n is max size of int, m is max ints stored
 * - No initialization allowed
 */


#include <stdio.h>
#include <stdlib.h>

#define N 100
#define M 10

typedef struct
{
    int table[N];
    int stack[M];
    int sp;
} FastSet;


FastSet* FastSet_new()
{
    FastSet *fs = malloc(sizeof(FastSet));
    fs->sp = 0;
    return fs;
}

int FastSet_insert(FastSet *fs, int x)
{
    if (FastSet_search(fs, x) < 1)
    {
        fs->table[x] = fs->sp;
        fs->stack[fs->sp++] = x;
    }
}

int FastSet_delete(FastSet *fs, int x)
{
    if (FastSet_search(fs, x) > 0)
    {
        int stackpos = fs->table[x];
        fs->table[x] = -1;
        fs->stack[stackpos] = fs->stack[fs->sp--];
    }
}

int FastSet_search(FastSet *fs, int x)
{
    if (fs->sp > 0)
    {
        int stackpos = fs->table[x];
        if (0 <= stackpos && stackpos < fs->sp)
        {
            if (fs->stack[stackpos] == x) 
            {
                return 1;
            }
        }
    }
    return 0;
}


int main()
{
    FastSet *fs = FastSet_new();
    FastSet_insert(fs, 2);
    FastSet_delete(fs, 2);
    FastSet_insert(fs, 1);
    FastSet_insert(fs, 1);
    printf("---\n");
    printf("%d\n", FastSet_search(fs, 1));
    printf("%d\n", FastSet_search(fs, 2));
    printf("%d\n", FastSet_search(fs, 3));
}

