#include "lists.h"
/**
 * check_cycle - function that checks if structure has a cycle
 * @list: the structure passed as argument
 * Return: 0 if no cycle, else 1
 */
int check_cycle(listint_t *list)
{
	char *str = (char *)(*list).next;
	int p = (*list).n, i = 0;

	for (; list != NULL; list = (*list).next)
	{
		if ((*list).next == NULL)
			break;
		if (i != 0 && strcmp((char *)(*list).next, str) == 0 && (*list).n == p)
			return (1);
		i++;
	}
	return (0);
}
